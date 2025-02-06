from PySide6 import QtWidgets
from PySide6.QtGui import QMovie, QFont, QFontDatabase
from APOLLO_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import QUrl, QByteArray, QJsonDocument
import subprocess
import json
import time


class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''Sets up the window and connects buttons'''
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("A.P.O.L.L.O")

        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handle_response)
        self.convo_history = ""
        self.Apollo_Sprite_idle_animation = QMovie("Assets\Apollo_Idle.gif")
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()
        self.Send_Button.clicked.connect(self.ask_ollama)

    def ask_ollama(self):
        '''Grabs prompt form input field and sends it to the ollama server'''
        self.query = self.Input_Field.toPlainText()
        self.Send_Button.setEnabled(False)
        self.start_time = time.time()

        url = QUrl("http://127.0.0.1:11434/api/generate")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader,
                          "application/json")

        json_data = {
            "model": "llama3.2:1b",
            "prompt": f"""You are a helpful AI assisant named APOLLO.
                          You are created by brayden cotterman, the user, who you refer to as Sir Cotterman.
                          You will answer questions with context from the conversation history and, of course, the user's question.
                          Conversation History: {self.convo_history}
                          Question: {self.query}""",
            "stream": True
        }

        byte_data = QByteArray(json.dumps(json_data).encode("utf-8"))

        # ✅ Print debugging information
        # print(f"Sending request to {url.toString()}")
        # print("Request Headers:", request.rawHeaderList())
        # print("JSON Payload:", json.dumps(json_data, indent=2))

        self.network_manager.post(request, byte_data)
        self.Apollo_Sprite_loading_animation = QMovie(
            "Assets\Apollo_Loading.gif")
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_loading_animation)
        self.Apollo_Sprite_loading_animation.start()

    def handle_response(self, reply: QNetworkReply):
        '''Handles the response from ollama and puts it in the chat display'''
        error_message = reply.errorString()
        status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)

        if error_message == QNetworkReply.NoError:
            response_data = reply.readAll().data().decode("utf-8")
            response = response_data.strip().split("\n")
            full_response = "".join(json.loads(
                resp)["response"] for resp in response)
        else:
            full_response = f"An error has occured: {error_message}\nStatus code: {status_code}"

        self.end_time = time.time()
        self.total_time = round(self.end_time - self.start_time)
        self.Response_Display.append(
            f"User: {self.query}\nAPOLLO: {full_response.strip()}\nResponse given in {self.total_time} seconds!")
        # print("✅ Response received:", full_response.strip())

        self.convo_history += f"User: {self.query}\nAPOLLO: {full_response.strip()}\n"
        self.Send_Button.setEnabled(True)
        self.Input_Field.clear()
        self.Apollo_Sprite_idle_animation = QMovie("Assets\Apollo_Idle.gif")
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()
