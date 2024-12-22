import numpy
import pyttsx3

class Apollo():
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[0].id) #? sets voice to gender 0 for male 1 for female
        
    def math(self):
        pass
    
    def speak(self, speech):
        self.engine.say(speech)
        self.engine.runAndWait()
        self.engine.stop()