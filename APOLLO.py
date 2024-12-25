import numpy
import pyttsx3
import speech_recognition as sr 
import openai

class Apollo():
    def __init__(self):
        self.app_is_running = True
        self.audio_recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
        self.speak(f"Hello, I am APOLLO! I am your voice assistant! Ask away!")
        self.main_loop()
        
    def main_loop(self):
        while self.app_is_running:
            
                self.listen()
                if self.user_input == "quit" or self.user_input == "cancel" or self.user_input == "deactivate":
                    self.speak("Powering ")
                    break
                
                else:
                    self.speak(f"User said: {self.user_input}")
                
    def math(self):
        pass
    
    def listen(self):
        with sr.Microphone() as source:
            self.speak("Listening. Hurry up!")
            self.audio = self.audio_recognizer.listen(source)
        
        try:
            self.user_input = self.audio_recognizer.recognize_google(self.audio)
            
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that.")
            
    def speak(self, speech):
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id) #? sets voice to gender 0 for male 1 for female
        self.engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)
        
        self.engine.say(speech)
        self.engine.runAndWait()
        self.engine.stop()