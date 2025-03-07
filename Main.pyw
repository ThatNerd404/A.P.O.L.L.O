from PySide6 import QtWidgets
from User_Interface import UserInterface
import sys
import multiprocessing
import os 
import subprocess

def start_ollama():
    subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW
    )
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()


if __name__ == "__main__":
    # ? makes it not print to screen when starting process

    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn", force=True)  # Prevent infinite subprocess spawns

    ollama_process = multiprocessing.Process(target=start_ollama)
    ollama_process.start()
    main()
    ollama_process.terminate()
    #! work around because ollama_server.kill fails to cancel the server
    os.system("taskkill /F /IM ollama.exe > nul 2>&1")
    
#TODO Make model to use for my job in lead generation
# * command to turn ui files into py files: pyside6-uic APOLLO_Mainwindow.ui > APOLLO_MainWindow.py make sure to be in powershell
# * command to turn py files into exe files: pyinstaller --onefile --noconsole pytoexe.py
#! remember to change encoding of the  ui-to-py files to utf-8 EVERY SINGLE TIME
#! REMEMBER YOU HAVE TO DELETE THE OLD PY FILE TO MAKE THE NEW ONE
#! Remember to make executable for yourself make sure to have absolute path or just keep it where it is and add idk a shortcut