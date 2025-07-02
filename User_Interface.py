from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PySide6.QtGui import QMovie, QKeyEvent, QFontDatabase, QKeySequence, QShortcut, QTextCursor
from PySide6.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from PySide6.QtCore import Qt, QPoint, QSettings, QEventLoop
from logging.handlers import RotatingFileHandler
from pathlib import Path
from APOLLO_MainWindow import Ui_MainWindow
from LlamaCPP import LlamaWorker
from TTS import TTSWorker
from Web_Scraper import WebScraper
import json
import logging
import time
import os

""" User Interface for APOLLO
    This script defines the user interface for the APOLLO application.
    It includes the main window, settings, and various functionalities such as saving and loading conversations.
    It uses the PySide6 library for the user interface and the logging library for logging."""

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Sets up the window and connects buttons"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("A.P.O.L.L.O")
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Setup cool pixel font
        self.font = QFontDatabase.addApplicationFont(
            os.path.join("Assets", "PixelPurl.ttf"))
        pixel_family = QFontDatabase.applicationFontFamilies(self.font)
        self.Input_Field.setFont(pixel_family[0])
        self.Response_Display.setFont(pixel_family[0])
        self.Font_Setting_CheckBox.setFont(pixel_family[0])
        self.Autosave_CheckBox.setFont(pixel_family[0])
        self.Memory_CheckBox.setFont(pixel_family[0])
        # Setup logger and rotating file handler
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(os.path.join(
            'Logs', 'log.log'), maxBytes=100000, backupCount=5, encoding="utf-8")
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Set up settings
        self.settings = QSettings("APOLLO", "Settings")
        
        # ? second value sets a default value if the key doesn't exist
        
        # Set checkboxes from saved values and initialize settings
        self.Font_Setting_CheckBox.setChecked(self.settings.value("Larger Font", False, type=bool))
        self.Autosave_CheckBox.setChecked(self.settings.value("AutoSave", False, type=bool))
        self.Memory_CheckBox.setChecked(self.settings.value("Memory", True, type=bool)) 
        self.apply_settings()
        
        # Initialize movie for idle animation and other animations
        self.Apollo_Sprite_idle_animation = QMovie(os.path.join("Assets", "Apollo_Idle.gif")
                                                   )
        self.Apollo_Sprite_loading_animation = QMovie(os.path.join(
            "Assets", "Apollo_Loading.gif"))
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

        # Connect signals or conditions to slots or functions
        self.Send_Button.clicked.connect(self.ask_llamacpp)
        self.Refresh_Button.clicked.connect(self.refresh_conversation)
        self.Save_Button.clicked.connect(self.save_conversation)
        self.Load_Button.clicked.connect(self.load_conversation)
        
        self.Change_Model_Button.clicked.connect(self.change_model)
        self.Settings_Button.clicked.connect(lambda: (self.logger.debug("Settings button clicked"), self.Settings_Button.isChecked()
                                                      and self.Main_Content.setCurrentIndex(1)
                                                      or not self.Settings_Button.isChecked()
                                                      and self.Main_Content.setCurrentIndex(0)
                                                      ))
        self.Apply_Changes_Button.clicked.connect(self.save_settings_and_apply)
        self.Close_Window_Button.clicked.connect(self.close)
        self.Minimize_Window_Button.clicked.connect(self.showMinimized)
        
        self.Input_Field.installEventFilter(self)

        # Initialize dragging variables for window movement
        self.is_dragging = False
        self.drag_start_position = QPoint()

        # Setup keyboard shortcuts
        Save_shortcut = QKeySequence(Qt.CTRL | Qt.Key_S)
        self.Save_SC = QShortcut(Save_shortcut, self)
        self.Save_SC.activated.connect(self.save_conversation)
        Load_shortcut = QKeySequence(Qt.CTRL | Qt.Key_L)
        self.Load_SC = QShortcut(Load_shortcut, self)
        self.Load_SC.activated.connect(self.load_conversation)
        Refresh_shortcut = QKeySequence(Qt.CTRL | Qt.Key_R)
        self.Refresh_SC = QShortcut(Refresh_shortcut, self)
        self.Refresh_SC.activated.connect(self.refresh_conversation)

        
        # Initialize variables for handling JSON data and conversations
        self.query = ""
        self.model = "mistral-7b-instruct-v0.2.Q2_K.gguf"  # ? default model change to not be hard-coded
        self.system_settings = f"""You are a helpful AI assisant named APOLLO. 
                          """
        self.convo_history = [
            {"role": "system", "content": self.system_settings}]
        self.convo_history_directory = Path(
            "C:\\Users\\MyCom\\Desktop\\.vscode\\Github_Projects\\A.P.O.L.L.O\\Conversations")
        self.current_response = ""
        self.logger.debug('Initialization finished')


    def save_to_memory(self, user_prompt, assistant_response):
        """Saves the content to a JSON file for long-term memory
           Args:
                user_prompt: The user's prompt
                assistant_response: The assistant's response"""
        self.logger.debug("save_to_memory was called")
        #* Save the content to a JSON file for long-term memory
        
        # ? check if the file exists, if not create it
        memory_path = "memory.json"
        if not os.path.exists(memory_path):
            with open(memory_path, "w") as f:
                json.dump([], f)
        # ? load the memory from the file
        with open(memory_path, "r") as f:
            memory = json.load(f)
        # ? check if the content is already in memory
        memory.append({"user": user_prompt,
    "assistant": assistant_response,
    "content": f"User: {user_prompt}\nAPOLLO: {assistant_response}"
    })
        with open(memory_path, "w") as f:
            json.dump(memory, f, indent=2)

        self.logger.info(f"New memory added. {user_prompt} -> {assistant_response}")
        
        

    def retrieve_relevant_memories(self, query, top_k=1):
        """Retrieves relevant memories from the JSON file based on the query
           Args: 
                query: The query to search for in the memories
                top_k: The number of top memories to retrieve"""
        self.logger.debug("retrieve_relevant_memories was called")
        
        memory_path = "memory.json"
        if not os.path.exists(memory_path):
            return []

        with open(memory_path, "r") as f:
            memory = json.load(f)

        docs = [m["content"] for m in memory]
        if not docs:
            return []
        # Use TF-IDF to find the most relevant memories
        # ? this is a simple way to do it, but you can use more advanced methods like embeddings
        vectorizer = TfidfVectorizer(lowercase=True,
        stop_words='english',  # remove "the", "and", etc.
        ngram_range=(1, 2),    # 1-grams and 2-grams = more overlap
        min_df=1      )
        vectors = vectorizer.fit_transform([query] + docs)
        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
        #self.logger.debug(
        #    f"Similarities: {similarities} \nQuery: {query} \nDocs: {docs}")
        # Get the indices of the top_k most similar memories
        
        top_indices = similarities.argsort()[-top_k:][::-1]
        self.logger.info(
            f"Relevant memories retrieved: {[docs[i] for i in top_indices]}")
        return [docs[i] for i in top_indices]



    def eventFilter(self, obj, event):
        """Detect Enter key in Input Field
           Args:
           obj: The object that the event is being sent to
           event: The event that is being sent"""
        if event.type() == QKeyEvent.KeyPress:
            if event.key() == Qt.Key_Return and not event.modifiers() & Qt.ShiftModifier and self.Send_Button.isEnabled:
                if not self.Input_Field.toPlainText().strip():  # ? stops from sending empty requests
                    return True
                else:
                    #? if the send button is checked, it will send the request
                    self.Send_Button.setChecked(True)
                    self.ask_llamacpp()
                    return True  # Prevent default behavior (optional)
        return super().eventFilter(obj, event)

    # Mouse press event to initiate dragging
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.is_dragging = True
            self.drag_start_position = event.globalPosition().toPoint() - \
                self.frameGeometry().topLeft()
            event.accept()

    # Mouse move event to handle dragging
    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPosition().toPoint() -
                      self.drag_start_position)
            event.accept()

    # Mouse release event to stop dragging
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            self.is_dragging = False
            event.accept()

    def closeEvent(self, event):
        """Handles the close event of the window"""
        self.logger.debug("closeEvent was called")
        if self.Autosave_CheckBox.isChecked():
            self.save_conversation()
        else:
            pass
        event.accept()
    
    def change_model(self):
        '''Changes the model based on the user's selection in the Model Chooser dropdown.'''
        self.logger.debug("change_model was called")
    
        Filename, ok = QFileDialog.getOpenFileName(
                self,
                "Select Model",
                os.path.join("Models"),
                "Models (*.*)"
            )

        # if the person doesn't select a file don't do anything
        if not Filename:
            pass
        else:
            self.logger.info(f"Model Chosen: {Filename}")
            self.model = os.path.basename(Filename)
            self.Response_Display.append(
                f"APOLLO: Model file: {self.model} loaded.")
            
        
        self.logger.info(
            f"Model changed to {self.model}")
        # ? reset the system settings
        self.convo_history[0] = {"role": "system",
                                 "content": self.system_settings}
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

    def ask_llamacpp(self):
        """Grabs prompt from input field and processes it with the Llama model."""
        if self.Send_Button.isChecked():
            self.logger.debug('ask_llamacpp called')

            # Get user's prompt and disable buttons
            self.query = self.Input_Field.toPlainText()
            self.Input_Field.clear()
            
            self.Refresh_Button.setEnabled(False)
            self.Save_Button.setEnabled(False)
            self.Load_Button.setEnabled(False)
            self.Change_Model_Button.setEnabled(False)
            self.Response_Display.setEnabled(False)
            
            # Add the user's prompt
            self.convo_history.append({"role": "user", "content": self.query})
            
            # Start loading animation
            self.Apollo_Sprite.setMovie(self.Apollo_Sprite_loading_animation)
            self.Apollo_Sprite_loading_animation.start()

            # Display response in UI element and ensure it scrolls
            self.Response_Display.append(f"User: {self.query}\nAPOLLO: ")
            self.cursor = self.Response_Display.textCursor()
            self.cursor.movePosition(QTextCursor.End)
            self.Response_Display.setTextCursor(self.cursor)
            
            # Retrieve relevant memories and insert into convo_history if available
            relevant_memories = self.retrieve_relevant_memories(self.query)
            if relevant_memories:
                memory_context = "\n".join(f"- {m}" for m in relevant_memories)
                self.convo_history.insert(1, {
                    "role": "system",
                    "content": f"This is a relevant past memory you have had. Use it to improve your response:\n{memory_context}"
                })
                
            # retrive web search results if the web search button is checked and 
            if self.Web_Search_Button.isChecked():
                self.logger.debug("Web Search Button is checked")
                self.web_scraper = WebScraper(self.query)
                
                self.web_scraper_loop = QEventLoop()
                
                self.web_scraper.finished.connect(
                    self.finish_WebSearch)
                self.web_scraper.error.connect(
                   self.web_scraper_error)
                self.web_scraper.start()
                
                self.web_scraper_loop.exec()  # Wait for the web scraper to finish
                
            self.logger.info(
                    f"Query sent: {self.query}\n Full request: {self.convo_history}")
            self.logger.debug(
                f"Model being used: {self.model}"
            )
            
            # Initialize the LlamaWorker with the model path and conversation history
            self.llama_worker = LlamaWorker(
                model_path=os.path.join("Models",self.model), 
                messages=self.convo_history,  # Use the conversation history as messages
                threads=6,  # Number of threads to use
                context=0,  # Use the model's default context size
                gpu_layers=0  # Number of GPU layers to use
            )
            
            # Connect signals to slots
            self.llama_worker.chunk_received.connect(self.update_response)
            self.llama_worker.finished.connect(self.finish_response)
            self.llama_worker.error.connect(self.llama_cpp_error)
            self.llama_worker.start()
            
            
            
            # grab start time
            self.start_time = time.perf_counter()
            
        else:
            
            self.cancel_request()
            
    def update_response(self, chunk):
        """Updates the response display with the chunk received from the LlamaWorker."""
        self.logger.debug("update_response was called")
        self.current_response += chunk
        self.Response_Display.insertPlainText(chunk)
        self.cursor = self.Response_Display.textCursor()
        self.cursor.movePosition(QTextCursor.End)
        self.Response_Display.setTextCursor(self.cursor)
        
    def finish_response(self):
        """Handles the completion of the response from the LlamaWorker."""
        self.logger.debug("finish_response was called")

        if self.TTS_Button.isChecked():
            self.tts_worker = TTSWorker(
                self.current_response, voice_id=None)  # Optional: specify a voice ID
            
            # log if worker fails or not
            self.tts_worker.finished.connect(
                lambda msg: self.logger.info(f"{msg}"))
            self.tts_worker.error.connect(
                lambda err: self.logger.error(f"{err}"))
            self.tts_worker.start()
        
        self.convo_history.append({"role": "assistant", "content": self.current_response})
        if self.settings.value("Memory", False, type=bool):
            self.save_to_memory(self.query, self.current_response)
        # Reset UI elements
        self.Send_Button.setChecked(False)
        self.Refresh_Button.setEnabled(True)
        self.Save_Button.setEnabled(True)
        self.Load_Button.setEnabled(True)
        self.Response_Display.setEnabled(True)
        self.Change_Model_Button.setEnabled(True)

        # Reset Apollo's animation to idle
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

        # Log completion message
        elapsed_time = time.perf_counter() - self.start_time
        self.logger.info(
            f"\nAPOLLO: Response completed in {elapsed_time:.2f} seconds.")
        
    def cancel_request(self):
        """Stops Apollo's response mid-stream by aborting the network request."""

        self.logger.debug("cancel_request was called")
        self.llama_worker.stop()
        # Reset UI elements
        self.Send_Button.setChecked(False)
        self.Refresh_Button.setEnabled(True)
        self.Save_Button.setEnabled(True)
        self.Load_Button.setEnabled(True)
        self.Response_Display.setEnabled(True)
        self.Change_Model_Button.setEnabled(True)

        # Reset Apollo's animation to idle
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

        # Display cancellation message
        self.Response_Display.append("\nAPOLLO: Response cancelled.")

        # reset current response
        self.current_response = ""

        # remove user query from history
        self.convo_history.pop()
    
    def llama_cpp_error(self, error):
        """Handles errors from the LlamaWorker."""
        self.logger.error(f"LlamaWorker encountered an error: {error}")
        self.Response_Display.append(f"APOLLO: An error occurred while processing your search request.\nError: {error}\nMoving forward without the response.")
        
    
    def finish_WebSearch(self, msg):
        """Handles the completion of the web search."""
        self.logger.debug("finish_WebSearch was called")
        self.logger.info(f"Web search completed with message: {msg}")
        # Add web search results to conversation history
        self.convo_history.insert(2,{"role": "system", "content": f"<web search information>{msg}</web search information>"})
        self.web_scraper_loop.exit()  # Stop the web scraper loop if it is running
        
    
            
    def web_scraper_error(self, error):
        """Handles errors from the WebScraper."""
        self.logger.error(f"WebScraper encountered an error: {error}")
        self.Response_Display.append(f"APOLLO: An error occurred while performing the web search.\nError: {error}")
        self.web_scraper_loop.exit()  # Stop the web scraper loop if it is running
        # Reset UI elements
        self.Send_Button.setChecked(False)
        self.Refresh_Button.setEnabled(True)
        self.Save_Button.setEnabled(True)
        self.Load_Button.setEnabled(True)
        self.Response_Display.setEnabled(True)
        self.Change_Model_Button.setEnabled(True)

        # Reset Apollo's animation to idle
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()
    def refresh_conversation(self):
        '''Clears the response display and empties the conversation history for speed and readability purposes'''
        self.logger.debug("refresh_conversation was called")
        if self.Refresh_Button.isEnabled:
            self.Input_Field.clear()
            self.Response_Display.clear()
            self.convo_history = [
                {"role": "system", "content": self.system_settings}]
        else:
            pass

    def save_conversation(self):
        '''Saves the current conversation display to a md file
           and the conversation history to a txt file'''
        # ? saves in a tuple of the text + a true boolean
        self.logger.debug("save_conversation was called")
        if self.Save_Button.isEnabled:
            savename, done = QInputDialog.getText(
                self, "File Name", "Enter File Name:")

            try:
                # if the person doesn't save to a file don't do anything
                if not savename:
                    pass
                else:
                    display_file = self.convo_history_directory / \
                        f"{savename}.md"

                    convo_file = self.convo_history_directory / \
                        f"{savename}.txt"
                    with open(display_file, "w") as df:
                        df.write(self.Response_Display.toPlainText().encode(
                            'ascii', 'ignore').decode('ascii'))
                    with open(convo_file, "w") as cf:
                        # ? encode to ignore emojis so the txt file can be read
                        for line in self.convo_history:
                            if isinstance(line["content"], str):
                                convo_history_no_emojis = {
                                    "role": line["role"], "content": line["content"].encode('ascii', 'ignore').decode('ascii')}
                            else:
                                convo_history_no_emojis = {
                                    "role": line["role"], "content": str(line["content"])}
                        json.dump(convo_history_no_emojis, cf)
                    self.Response_Display.append(
                        f"APOLLO: Conversation Saved to file {savename}.md")
                    self.logger.info(f"Conversation saved to file: {savename}")

            except Exception as e:
                self.Response_Display.append("""APOLLO: Filename not workable. Remember no back slashes, spaces, or special characters!
                Try again and fit the requirements.""")
                self.logger.error(
                    f"Filename {self.convo_history_directory / savename} not working.\n Exception: {e}")
                self.save_conversation()
        else:
            pass

    def load_conversation(self):
        """Loads past conversation history into the json requests and loads past display history"""
        if self.Load_Button.isEnabled:

            self.logger.debug("load_conversation was called")
            Filename, ok = QFileDialog.getOpenFileName(
                self,
                "Select Conversation",
                os.path.join("Conversations"),
                "Conversations (*.md)"
            )

            # if the person doesn't select a file don't do anything
            if not Filename:
                pass

            else:
                self.logger.info(f"File opened: {Filename}")
                self.refresh_conversation()
                self.Response_Display.append(
                    f"APOLLO: Conversation file:{Filename} loaded.")

                # Completely empty convo history file because the other file will already have the basic system prompt
                self.convo_history = []
                try:
                    # open display history file and append to response display
                    with open(Filename, "r") as dh:
                        self.display_history = dh.read()
                    self.Response_Display.append(self.display_history)
                    name, ext = os.path.splitext(Filename)

                    # open convo history file and append to convo history
                    with open(f"{name}.txt", "r") as sh:
                        self.convo_history = json.load(sh)
                    self.logger.info(
                        f"new convo history loaded: {self.convo_history}")

                except Exception as e:
                    self.Response_Display.append(
                        """APOLLO: Filename not opening.""")
                    self.logger.error(
                        f"Filename {Filename} not opening correctly.\n Exception: {e}")
        else:
            pass

    def apply_settings(self):
        """Applies settings to the UI"""

        self.logger.debug("apply_settings was called")

        # Check for larger font setting and apply it
        

        # ? for some reason the settings value is a string so we have to check if it is true or false by checking the string value
        if self.settings.value("Larger Font", False, type=bool):
            self.Input_Field.setStyleSheet(
                "background-color: #243169; border-color:#98c5de; border-style: solid; border-width: 5px; font-size: 32px;")
            self.Response_Display.setStyleSheet(
                "background-color: #243169; border-color:#98c5de; border-style: solid; border-width: 5px; font-size: 48px;")
            self.logger.info("Larger font setting applied")

        else:
            self.Input_Field.setStyleSheet(
                " background-color: #243169; border-color:#98c5de; border-style: solid; border-width: 5px; font-size: 16px;")
            self.Response_Display.setStyleSheet(
                "background-color: #243169; border-color:#98c5de; border-style: solid; border-width: 5px; font-size: 32px;")
            self.logger.info("Larger font setting removed")

        

        if self.settings.value("AutoSave", False, type=bool):
            self.logger.info("Auto save setting applied")
            
        else:
            self.logger.info("Auto save setting removed")
            
        # Check for memory setting and apply it
        if self.settings.value("Memory", False, type=bool):
            self.logger.info("Memory setting applied")
            
        else:
            self.logger.info("Memory setting removed")

    def save_settings_and_apply(self):
        self.logger.debug("save_settings_and_apply was called")

        # Save the current checkbox states
        self.settings.setValue("Larger Font", self.Font_Setting_CheckBox.isChecked())
        self.settings.setValue("AutoSave", self.Autosave_CheckBox.isChecked())
        self.settings.setValue("Memory", self.Memory_CheckBox.isChecked())  # optional

        self.logger.debug(f"Saved settings: Larger Font={self.Font_Setting_CheckBox.isChecked()}, "
                        f"AutoSave={self.Autosave_CheckBox.isChecked()}, "
                        f"Memory={self.Memory_CheckBox.isChecked()}")

        # Then apply them
        self.apply_settings()