import numpy
import pyttsx3

class Apollo():
    def __init__(self):
        self.app_is_running = True
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id) #? sets voice to gender 0 for male 1 for female
        self.engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)
        self.speak(f"Hello, I am APOLLO! I am your voice assistant! Ask away!")
        self.main_loop()
        
    def main_loop(self):
        while self.app_is_running:
            user_input = input("")
            
            if user_input.lower() == "quit" or user_input.lower() == "q":
                self.speak(f"Bye Asshole")
                self.app_is_running = False
            
            elif user_input.lower() == "math":
                self.math()
           
            else:
                self.speak(f"You haven't programmed me to do anything yet fuck wad.")
                
    def math(self):
        self.speak(f"Type Your question?")
        question = input()
        self.speak(f"I have no clue how to answer that jackass! how about you program me to do that!")
        
    def speak(self, speech):
        self.engine.say(speech)
        self.engine.runAndWait()
        self.engine.stop()