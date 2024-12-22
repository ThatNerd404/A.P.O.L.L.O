import numpy
import pyttsx3

class Apollo():
    def __init__(self):
        self.engine = pyttsx3.init()
        
    def math(self):
        pass
    
    def speak(self, speech):
        self.engine.say(speech)
        self.engine.runAndWait()