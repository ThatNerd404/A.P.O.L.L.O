import numpy
import pyttsx3

class Apollo():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id) #? sets voice to gender 0 for male 1 for female
        self.engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)
        self.math()
    
    def main_loop(self):
        pass
    
    def math(self):
        answer = str(5 + 5)
        self.speak(f"5 + 5 equals {answer}")
        
    def speak(self, speech):
        self.engine.say(speech)
        self.engine.runAndWait()
        self.engine.stop()