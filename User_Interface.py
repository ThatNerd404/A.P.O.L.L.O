from PySide6 import QtWidgets
from PySide6.QtCore import QThread
from APOLLO_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl, QByteArray
import subprocess


class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # ? setup window
        self.setupUi(self)
        self.setWindowTitle("A.P.O.L.L.O")
        # ? planned text color #6a93be
        self.ollama_process = subprocess.Popen(
            ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        #! remember to close process after and max thing to close process