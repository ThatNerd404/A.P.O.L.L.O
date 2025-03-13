from PySide6.QtGui import QMovie, QKeyEvent, QFontDatabase, QKeySequence, QShortcut
from PySide6.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl, QByteArray, Qt
from logging.handlers import RotatingFileHandler
from pathlib import Path
from APOLLO_MainWindow import Ui_MainWindow
import json
import logging
import time
import os


class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Sets up the window and connects buttons"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("A.P.O.L.L.O")
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Setup cool pixel font
        font = QFontDatabase.addApplicationFont(
            os.path.join("Assets", "PixelPurl.ttf"))
        pixel_family = QFontDatabase.applicationFontFamilies(font)
        self.Model_Chooser.setFont(pixel_family[0])
        self.Input_Field.setFont(pixel_family[0])
        self.Response_Display.setFont(pixel_family[0])

        # Setup logger and rotating file handler
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(os.path.join(
            'Logs', 'log.log'), maxBytes=100000, backupCount=5)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Initialize network manager
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handle_response)

        # Initialize movie for idle animation and other animations
        self.Apollo_Sprite_idle_animation = QMovie(os.path.join("Assets", "Apollo_Idle.gif")
                                                   )
        self.Apollo_Sprite_loading_animation = QMovie(os.path.join(
            "Assets", "Apollo_Loading.gif"))
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

        # Connect signals or conditions to slots or functions
        self.Send_Button.clicked.connect(self.ask_ollama)
        self.Refresh_Button.clicked.connect(self.refresh_conversation)
        self.Save_Button.clicked.connect(self.save_conversation)
        self.Load_Button.clicked.connect(self.load_conversation)
        self.Cancel_Button.clicked.connect(self.cancel_request)
        self.Close_Window_Button.clicked.connect(self.close)
        self.Minimize_Window_Button.clicked.connect(self.showMinimized)
        self.Model_Chooser.currentIndexChanged.connect(
            self.change_model)
        self.Input_Field.installEventFilter(self)

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
        self.partial_json_buffer = ""
        self.query = ""
        self.model = "phi4-mini"
        self.system_settings = f"""You are a helpful AI assisant named APOLLO. You refer to the user as Sir Cotterman.
                          """
        self.convo_history = [
            {"role": "system", "content": self.system_settings}]
        self.convo_history_directory = Path(
            "C:\\Users\\MyCom\\Desktop\\.vscode\\Github_Projects\\A.P.O.L.L.O\\Conversations")
        self.current_response = ""
        self.logger.debug('Initialization finished')

    def eventFilter(self, obj, event):
        """Detect Enter key in Input Field"""
        if event.type() == QKeyEvent.KeyPress:
            if event.key() == Qt.Key_Return and not event.modifiers() & Qt.ShiftModifier and self.Send_Button.isEnabled:
                if not self.Input_Field.toPlainText().strip():  # ? stops from sending empty requests
                    return True
                else:
                    self.ask_ollama()
                    return True  # Prevent default behavior (optional)
        return super().eventFilter(obj, event)

    def ask_ollama(self):
        """Grabs prompt from input field and sends it to the ollama server"""
        if self.Send_Button.isEnabled:
            self.logger.debug('ask_ollama called')

            # Get user's prompt and disable buttons
            self.query = self.Input_Field.toPlainText()
            self.Input_Field.clear()
            self.Send_Button.setEnabled(False)
            self.Refresh_Button.setEnabled(False)
            self.Save_Button.setEnabled(False)
            self.Model_Chooser.setEnabled(False)
            self.Load_Button.setEnabled(False)
            # Add the user's prompt
            self.convo_history.append({"role": "user", "content": self.query})

            # Create request URL and set header
            url = QUrl("http://127.0.0.1:11434/api/chat")
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader,
                              "application/json")

            # Create JSON data to send to server
            self.json_data = {
                "model": self.model,
                "messages": self.convo_history,
                # ? temperature makes the answer a bit more random
                "options": {"temperature": 0.7},
                "keep_alive": "5m",  # ? '0' or 0 instantly deloads model after completion of request -1 or "-1" loads the model indefinitely
                "stream": True,
            }

            self.logger.info(
                f"Query sent: {self.query}\n Full json request: {self.json_data}")

            # Convert JSON data to bytes and set as body of the request
            byte_data = QByteArray(json.dumps(self.json_data).encode("utf-8"))
            self.reply = self.network_manager.post(request, byte_data)

            # Connect readyRead signal to handleResponse method
            self.reply.readyRead.connect(self.handle_response)

            # Start loading animation
            self.Apollo_Sprite.setMovie(self.Apollo_Sprite_loading_animation)
            self.Apollo_Sprite_loading_animation.start()

            # Display response in UI element
            self.Response_Display.append(f"User: {self.query}\nAPOLLO: ")

            # grab start time
            self.start_time = time.perf_counter()
        else:
            pass

    def handle_response(self):
        """
        Handles the response from ollama and puts it in the chat display.

        Note: The code assumes that the raw data received is a JSON object with a "message" key, and an optional "done" key indicating whether the conversation is complete.
        """

        #!error_message = self.reply.errorString()
        #!status_code = self.reply.attribute(
        #!    QNetworkRequest.HttpStatusCodeAttribute)
        raw_data = self.reply.readAll().data().decode()
        self.partial_json_buffer += raw_data

        while "\n" in self.partial_json_buffer:
            line, self.partial_json_buffer = self.partial_json_buffer.split(
                "\n", 1)
            line = line.strip()

            if not line:
                continue

            try:
                json_obj = json.loads(line)

                # ? If "response" key is present in the JSON object, insert it into the chat display
                if "message" in json_obj and "content" in json_obj["message"]:
                    chunk = json_obj["message"]["content"]
                    self.current_response += chunk  # Append the chunk
                    self.Response_Display.ensureCursorVisible()
                    self.Response_Display.insertPlainText(
                        chunk)  # Stream it to UI
                    self.Response_Display.ensureCursorVisible()

                # ? If "done" key is present in the JSON object and it's set to True, finalize the response
                if json_obj.get("done", False):
                    # grab end time and log it
                    self.end_time = time.perf_counter()
                    elasped_time = self.end_time - self.start_time
                    self.logger.info(
                        f"Response finished generating in {elasped_time:.4f} seconds")

                    # ? decode to ignore emojis
                    self.logger.info(
                        f"Full APOLLO response: {self.current_response.encode('ascii', 'ignore').decode('ascii')}")

                    # re-enable buttons
                    self.Send_Button.setEnabled(True)
                    self.Refresh_Button.setEnabled(True)
                    self.Save_Button.setEnabled(True)
                    self.Model_Chooser.setEnabled(True)
                    self.Load_Button.setEnabled(True)
                    # add APOLLO response to convo history
                    self.convo_history.append(
                        {"role": "assistant", "content": self.current_response})

                    self.Apollo_Sprite.setMovie(
                        self.Apollo_Sprite_idle_animation)
                    self.Apollo_Sprite_idle_animation.start()
                    self.current_response = ""
                    self.reply.abort()

            except json.JSONDecodeError as e:
                self.logger.error("❌ JSON Decode Error:", e,
                                  "Raw Line:", repr(line))
    
    def cancel_request(self):
        """Stops Apollo's response mid-stream by aborting the network request."""

        if hasattr(self, "reply") and self.reply.isRunning() and self.reply:
            self.reply.abort()  # Cancel the ongoing network request
            self.logger.info("Response cancelled")
            # Reset UI elements
            self.Send_Button.setEnabled(True)
            self.Refresh_Button.setEnabled(True)
            self.Save_Button.setEnabled(True)
            self.Load_Button.setEnabled(True)
            self.Model_Chooser.setEnabled(True)

            # Reset Apollo's animation to idle
            self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
            self.Apollo_Sprite_idle_animation.start()

            # Display cancellation message
            self.Response_Display.append("\nAPOLLO: Response cancelled.")

            # reset current response
            self.current_response = ""

            # remove user query from history
            self.convo_history.pop()
        else:
            self.Response_Display.append(
                "\nAPOLLO: No response being generated currently.")
            self.logger.debug(
                "cancel_request has been run when no response is being generated.")

    
    
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

    def change_model(self):
        '''Updates the prompt with the query and changes the prompt if the apollo model changes'''
        self.logger.debug("change_model was called")
        # Get the current text of the Model Chooser combo box
        chosen_model = self.Model_Chooser.currentText()

        # Update the model, prompt, and sprite based on the selected choice
        if chosen_model.strip() == "General":
            self.model = "phi4-mini"
            self.system_settings = """You are a helpful AI assisant named APOLLO.\n
                          You refer to the user as Sir Cotterman.
                          """
            self.Apollo_Sprite_idle_animation = QMovie(os.path.join(
                "Assets", "Apollo_Idle.gif"))
            self.Apollo_Sprite_loading_animation = QMovie(os.path.join(
                "Assets", "Apollo_Loading.gif"))

        elif chosen_model.strip() == "Coding":
            self.model = "qwen2.5-coder:3b"
            self.system_settings = """You are APOLLO.\n
                          Talk in a gritty punk persona, using slang and street speak like you would hear in the game Cyberpunk 2077.\n
                          The tone should be dark, rebellious, and intense..\n
                          You refer to the user as Mr Cotterman.\n
                          """
            self.Apollo_Sprite_idle_animation = QMovie(os.path.join(
                "Assets", "Apollo_Idle_Coding.gif"))
            self.Apollo_Sprite_loading_animation = QMovie(os.path.join(
                "Assets", "Apollo_Loading_Coding.gif"))

        elif chosen_model.strip() == "Tutoring":
            self.model = "phi4-mini"
            self.system_settings = """You are a helpful AI assisant named APOLLO.\n
                          You refer to the user as Sir Cotterman.\n
                          You will act as a Socratic tutor and first give me a very in-depth explanation of my question\n
                          then give me examples, then give sources to help allow the user to research for themselves,\n
                          then ask me questions about it to help me build understanding.\n
                          """

            self.Apollo_Sprite_idle_animation = QMovie(os.path.join(
                "Assets", "Apollo_Idle_Tutoring.gif"))
            self.Apollo_Sprite_loading_animation = QMovie(os.path.join(
                "Assets", "Apollo_Loading_Tutor.gif"))

        self.logger.info(
            f"Model changed to {self.model}\nSystem settings changed to {self.system_settings}")
        # ? reset the system settings
        self.convo_history[0] = {"role": "system",
                                 "content": self.system_settings}
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

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
                        df.write(self.Response_Display.toPlainText())
                    with open(convo_file, "w") as cf:
                        json.dump(self.convo_history,cf)
                    self.Response_Display.append(
                        f"APOLLO: Conversation Saved to file {savename}.md")
                    self.logger.info(f"Conversation saved to file: {savename}")

            except Exception as e:
                self.Response_Display.append("""APOLLO: Filename not workable. Remember no back slashes, spaces, or special characters!
                Try again and fit the requirements.""")
                self.logger.error(f"Filename {savename} not working.\n Exception: {e}")
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
                self.Response_Display.append(f"APOLLO: Conversation file:{Filename} loaded.")
                
                # Completely empty convo history file because the other file will already have the basic system prompt
                self.convo_history = []
                try:
                    with open(Filename, "r") as dh:
                        self.display_history = dh.read()
                    self.Response_Display.append(self.display_history)
                    name, ext = os.path.splitext(Filename)
                    
                    with open(f"{name}.txt", "r") as sh:
                        self.convo_history = json.load(sh)
                    self.logger.info(f"new convo history loaded: {self.convo_history}")
                    
                
                except Exception as e:
                        self.Response_Display.append("""APOLLO: Filename not opening.""")
                        self.logger.error(f"Filename {Filename} not opening correctly.\n Exception: {e}")
        else:
            pass