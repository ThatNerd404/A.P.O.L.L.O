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

        self.Apollo_Sprite_idle_animation = QMovie("Assets\Apollo_Idle.gif")
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_idle_animation)
        self.Apollo_Sprite_idle_animation.start()
        self.Send_Button.clicked.connect(self.ask_ollama)
        self.partial_json_buffer = ""
        self.query = ""
        self.convo_history = ""

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

        self.reply = self.network_manager.post(request, byte_data)
        self.reply.readyRead.connect(self.handle_response)

        self.Apollo_Sprite_loading_animation = QMovie(
            "Assets\Apollo_Loading.gif")
        self.Apollo_Sprite.setMovie(self.Apollo_Sprite_loading_animation)
        self.Apollo_Sprite_loading_animation.start()

        self.Response_Display.append(f"User: {self.query}\nAPOLLO: ")

    def handle_response(self):
        '''Handles the response from ollama and puts it in the chat display'''
        error_message = self.reply.errorString()
        status_code = self.reply.attribute(
            QNetworkRequest.HttpStatusCodeAttribute)
        raw_data = self.reply.readAll().data().decode()

        self.partial_json_buffer += raw_data

        while "\n" in self.partial_json_buffer:
            line, self.partial_json_buffer = self.partial_json_buffer.split(
                "\n", 1)
            line = line.strip()

            if not line:
                continue

            if line:
                try:
                    json_obj = json.loads(line)

                    if "response" in json_obj:
                        self.Response_Display.insertPlainText(
                            json_obj["response"])  # ✅ Stream output
                        self.Response_Display.ensureCursorVisible()
                    # ✅ If "done" is True, finalize response
                    if json_obj.get("done", False):
                        self.Send_Button.setEnabled(True)
                        self.Input_Field.clear()
                        self.end_time = time.time()
                        self.total_time = round(
                            self.end_time - self.start_time)
                        self.Apollo_Sprite_idle_animation = QMovie(
                            "Assets\Apollo_Idle.gif")
                        self.Apollo_Sprite.setMovie(
                            self.Apollo_Sprite_idle_animation)
                        self.Apollo_Sprite_idle_animation.start()
                        self.convo_history += self.Response_Display.toPlainText()

                except json.JSONDecodeError as e:
                    print("❌ JSON Decode Error:", e, "Raw Line:", repr(line))
