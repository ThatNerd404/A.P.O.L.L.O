from PySide6 import QtWidgets
from User_Interface_CPP import UserInterface
import sys

""" Main script for APOLLO
    This script serves as the entry point for the APOLLO application.
    It initializes the user interface
"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
    
#TODO Make model to use for my job in lead generation
# * command to turn ui files into py files: pyside6-uic APOLLO_Mainwindow.ui > APOLLO_MainWindow.py make sure to be in powershell
# * command to turn py files into exe files: pyinstaller --onefile --noconsole pytoexe.py
#! remember to change encoding of the  ui-to-py files to utf-8 EVERY SINGLE TIME
#! Remember to make executable for yourself make sure to have absolute path or just keep it where it is and add idk a shortcut
#! REMEMBER YOU HAVE TO DELETE THE OLD PY FILE TO MAKE THE NEW ONE