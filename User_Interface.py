from PySide6.QtGui import QMovie
from APOLLO_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl, QByteArray
import json
import logging

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Sets up the window and connects buttons"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("A.P.O.L.L.O")

        # Initialize network manager
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handle_response)

        # Initialize movie for idle animation and other animations
        self.Apollo_Sprite_idle_animation = QMovie(
            "Assets\Apollo_Idle.gif")
        self.Apollo_Sprite_loading_animation = QMovie(
            "Assets\Apollo_Loading.gif")
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()

        # Connect buttons to functions
        self.Send_Button.clicked.connect(self.ask_ollama)
        self.Refresh_Button.clicked.connect(self.refresh_conversation)
        self.Model_Chooser.currentIndexChanged.connect(
            self.change_model)

        # Initialize variables for handling JSON data and conversations
        self.partial_json_buffer = ""
        self.MAX_TOKEN = 1000
        self.query = ""
        self.model = "llama3.2:1b"
        self.system_settings = f"""You are a helpful AI assisant named APOLLO. You are created by brayden cotterman,
                          the user, who you refer to as Sir Cotterman.
                          """
        self.convo_history = [
            {"role": "system", "content": self.system_settings}]

    def ask_ollama(self):
        """Grabs prompt from input field and sends it to the ollama server"""

        # Get user's prompt and disable buttons
        self.query = self.Input_Field.toPlainText()
        self.Input_Field.clear()
        self.Send_Button.setEnabled(False)
        self.Refresh_Button.setEnabled(False)
        self.Model_Chooser.setEnabled(False)
        
        # Update the prompt
        self.convo_history.append({"role": "user", "content": self.query})

        # Create request URL and set header
        url = QUrl("http://127.0.0.1:11434/api/chat")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader,
                          "application/json")
        
        # Create JSON data to send to server
        self.json_data = {
            "model": self.model,
            "messages": self.convo_history, #TODO: add a  {"role": "system", "content": relevant documents using rag}
            "options": {"temperature": 0.7}, # ? temperature makes the answer a bit more random
            "keep_alive": "5m", #? '0' or 0 instantly deloads model after completion of request -1 or "-1" loads the model indefinitely
            "stream": True,
        }

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
        self.current_response = ""
        
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
                    self.Response_Display.insertPlainText(chunk)  # Stream it to UI
                    self.Response_Display.ensureCursorVisible()
                    
                # ? If "done" key is present in the JSON object and it's set to True, finalize the response
                if json_obj.get("done", False):
                    self.Send_Button.setEnabled(True)
                    self.Refresh_Button.setEnabled(True)
                    self.Model_Chooser.setEnabled(True)
                    
                    
                    self.convo_history.append({"role": "assistant", "content": self.current_response})
                    
                    self.current_response = ""
                    self.Apollo_Sprite.setMovie(
                        self.Apollo_Sprite_idle_animation)
                    self.Apollo_Sprite_idle_animation.start()

            except json.JSONDecodeError as e:
                print("❌ JSON Decode Error:", e, "Raw Line:", repr(line))

    def refresh_conversation(self):
        '''Clears the response display and empties the conversation history for speed and readability purposes'''
        self.Input_Field.clear()
        self.Response_Display.clear()
        self.convo_history = [
            {"role": "system", "content": self.system_settings}]
        self.Response_Display.append("APOLLO: Conversation history refreshed.")

    def change_model(self):
        '''Updates the prompt with the query and changes the prompt if the apollo model changes'''
        self.refresh_conversation()
        
        # Get the current text of the Model Chooser combo box
        chosen_model = self.Model_Chooser.currentText()
        
        # Update the model, prompt, and sprite based on the selected choice
        if chosen_model == "General":
            self.model = "llama3.2:1b"
            self.system_settings = """You are a helpful AI assisant named APOLLO.
                          You are created by brayden cotterman, the user, who you refer to as Sir Cotterman.
                          Remember to use the conversation history to inform your answer only.
                          """
            self.Apollo_Sprite_idle_animation = QMovie(
            "Assets\Apollo_Idle.gif")
            self.Apollo_Sprite_loading_animation = QMovie(
            "Assets\Apollo_Loading.gif")
            
        elif chosen_model == "Coding":
            self.model = "codellama:7b"
            self.system_settings = """You are a helpful AI assisant named APOLLO.
                          You are created by brayden cotterman, the user, who you refer to as Sir Cotterman.
                          Take the following code and add comments to it to improve readability and make it adhere to pep8 standards."""
            self.Apollo_Sprite_idle_animation = QMovie(
            "Assets\Apollo_Idle_Coding.gif")
            self.Apollo_Sprite_loading_animation = QMovie(
            "Assets\Apollo_Loading_Coding.gif")

        elif chosen_model == "Tutoring":
            self.model = "llama3.2:1b"
            self.system_settings = """You are a helpful AI assisant named APOLLO.
                          You are created by brayden cotterman, the user, who you refer to as Sir Cotterman.
                          You will act as a Socratic tutor and first give me a very in-depth explanation of my question
                          then give me examples, then give sources to help allow the user to research for themselves, 
                          then ask me questions about it to help me build understanding.
                          Remember to use the conversation history to inform your answer only.
                          """
                          
            self.Apollo_Sprite_idle_animation = QMovie(
            "Assets\Apollo_Idle_Tutoring.gif")
            self.Apollo_Sprite_loading_animation = QMovie(
            "Assets\Apollo_Loading_Tutor.gif")
            
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()
        
    def save_conversation(self):
        '''Saves the conversation to a txt file'''
        pass
