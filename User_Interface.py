from PySide6 import QtWidgets
from PySide6.QtCore import QThread
from APOLLO_MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #? setup window
        self.setupUi(self)
        self.setWindowTitle("APOLLO")