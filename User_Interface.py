from PySide6 import QtWidgets
from PySide6.QtCore import QThread
from APOLLO_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtCore import QUrl, QByteArray, QJsonDocument
import subprocess
import json

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # ? setup window
        self.setupUi(self)
        self.setWindowTitle("A.P.O.L.L.O")
        # ? planned text color #6a93be
        '''self.ollama_process = subprocess.Popen(
            ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )'''
        # Qt's asynchronous HTTP request manager
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handle_response)

        self.Send_Button.clicked.connect(self.ask_ollama)
        
    def ask_ollama(self):
        self.prompt = self.Input_Field.toPlainText()
        self.Send_Button.setEnabled(False)
        
        url = QUrl("http://127.0.0.1:11434/api/generate")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        json_data = {
            "model": "llama3.2:1b",
            "prompt": self.prompt,
        }

        byte_data = QByteArray(json.dumps(json_data).encode("utf-8"))
    
        # ✅ Print debugging information
        #print(f"Sending request to {url.toString()}")
        #print("Request Headers:", request.rawHeaderList())
        #print("JSON Payload:", json.dumps(json_data, indent=2))

        self.network_manager.post(request, byte_data)
        
        
        
    def handle_response(self, reply: QNetworkReply):
        """Handles the response from Ollama asynchronously."""
        error_message = reply.errorString()
        status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute) 
        response_data = reply.readAll().data().decode("utf-8")
        response = response_data.strip().split("\n")
        full_response = "".join(json.loads(resp)["response"] for resp in response)
        self.Response_Display.append(f"User: {self.prompt}\nAPOLLO: {full_response.strip()}\n")
        #print("✅ Response received:", full_response.strip())
           

        self.Send_Button.setEnabled(True)  # Re-enable button
        self.Input_Field.clear()