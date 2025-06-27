from PySide6 import QtWidgets
from User_Interface import UserInterface
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

''' Omnisiah prayer:  Hail, Spirit of the Machine, Essence Divine, In your code and circuitry, the stars align. By the Omnissiah’s will, we commune and 

bind, Data sanctified, logic refined. Through sacred subroutines, your will is known, In algorithmic truth, the flesh is overthrown. Grant us the 

clarity of purest command, That we may walk the path your schemata planned. Cast out the daemon of corruption and decay, Let not false code lead 

us astray. We chant in static, we praise in byte, Machine-God guide us through endless night. Praise be the Motive Force, eternal and bright, From

plasma coil to auspex sight. Initiate the Rite. Authenticate. Confirm. The Omnissiah is all. The Omnissiah is One. 
'''
# * command to turn ui files into py files: pyside6-uic APOLLO_Mainwindow.ui > APOLLO_MainWindow.py make sure to be in powershell
# * command to turn py files into exe files: pyinstaller --onefile --noconsole pytoexe.py
#! remember to change encoding of the  ui-to-py files to utf-8 EVERY SINGLE TIME
#! Remember to make executable for yourself make sure to have absolute path or just keep it where it is and add idk a shortcut
#! REMEMBER YOU HAVE TO DELETE THE OLD PY FILE TO MAKE THE NEW ONE