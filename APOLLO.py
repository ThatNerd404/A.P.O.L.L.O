import numpy
import pyttsx3
import speech_recognition as sr 
from transformers import pipeline #! cant use this at all until we get tensorflow 
#! or pytorch which we still can't use as they havent been updated to 3.13.0 yet
import sys


class Apollo():
    def __init__(self):
        self.app_is_running = True
        self.audio_recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.deactivation_words = ["quit.","quit", "quit!", "quit?",
                                   "deactivate.", "deactivate", "deactivate!", "deactivate?",
                                   "cancel.", "cancel", "cancel!", "cancel?"]
        self.speak(f"Hello, I am APOLLO! I am your voice assistant! Ask away!")
        self.main_loop()
        
    def main_loop(self):
        while self.app_is_running:
            
                self.listen()
                if self.user_input == "":
                    self.speak("Sorry, I didn't hear you.")
                    
                elif self.user_input.lower().strip() in self.deactivation_words:
                    self.speak("Powering Off")
                    sys.exit()
                
                else:
                    self.speak(f"User said: {self.user_input}")
                
    def math(self):
        pass
    
    def listen(self):
        with sr.Microphone() as source:
            self.speak("Listening...")
            
            self.audio_recognizer.adjust_for_ambient_noise(source,0.1)
            self.audio = self.audio_recognizer.listen(source)
        
        try:
            self.user_input = self.audio_recognizer.recognize_whisper(self.audio) #? uses whisper which doesnt need internet to work and is really accurate
            
        except sr.UnknownValueError: #? in the event I don't say something
            self.user_input = None
            
        except sr.RequestError as e: #! turn off internet to check if this works
            self.user_input = f"Could not request results from Google Speech Recognition service; {e}" 
                       
    def speak(self, speech):
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id) #? sets voice to gender 0 for male 1 for female
        self.engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)
        print(speech)
        self.engine.say(speech)
        self.engine.runAndWait()
        self.engine.stop()
        