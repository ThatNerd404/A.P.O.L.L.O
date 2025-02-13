from PySide6 import QtWidgets
from User_Interface import UserInterface
import sys
#import subprocess

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    app.exec()


if __name__ == "__main__":
    # ? makes it not print to screen when starting process
    # ollama_server = subprocess.Popen(    ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    # ollama_server.kill()

'''import requests

url = "http://127.0.0.1:11434/api/generate"
json_data = {
    "model": "llama3.2:1b",
    "prompt": "Hello",
    "stream": True
}

response = requests.post(url, json=json_data, stream=True)
for line in response.iter_lines():
    print("Response:", line)'''

# * command to turn ui files into py files: pyside6-uic APOLLO_Mainwindow.ui > APOLLO_MainWindow.py make sure to be in powershell
# * command to turn py files into exe files: pyinstaller --onefile -w pytoexe.py
#! remember to change encoding of the  ui-to-py files to utf-8 EVERY SINGLE TIME
#! REMEMBER YOU HAVE TO DELETE THE OLD PY FILE TO MAKE THE NEW ONE
#! Remember to make executable for yourself make sure to have absolute path or just keep it where it is and add idk a shortcut