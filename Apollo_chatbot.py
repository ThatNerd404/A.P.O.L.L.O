
from Settings import *

class Apollo_ChatBot():
    def __init__(self):
        self.app_is_running = True
        self.speak(f"Hello, I am APOLLO! I am your voice assistant! Ask away!")
        
        
    def run(self):
        
        self.speak("Alright let's talk!")
        self.listen()
        conversation = self.user_voice
        while True:
            if self.user_voice.lower().strip() in deactivation_words:
                self.speak("Powering Off...")
                break
            self.speak("Thinking...")
            conversation = chatbot(conversation)[0]['generated_text']
            self.speak(conversation)
            self.listen()
            conversation = self.user_voice
            if self.user_voice.lower().strip() in deactivation_words:
                self.speak("Powering Off...")
                break
            else:
                continue
            
                
        
    
    def listen(self):
        with sr.Microphone() as source:
            self.speak("Listening...")
            
            
            try:
                audio_recognizer.adjust_for_ambient_noise(source,0.5)
                self.audio = audio_recognizer.listen(source, timeout=10)
        
                self.user_voice = audio_recognizer.recognize_whisper(self.audio) #? uses whisper which doesnt need internet to work and is really accurate
                if self.user_voice == "":
                    self.speak("I'm sorry I didn't hear you?")
                    self.listen()
                else:
                    pass
                
            except sr.WaitTimeoutError:
                self.speak("I'm sorry I didn't hear you?")
                print("Wait time Error")
                self.listen()
                
    def speak(self, speech):
        print(speech)
        tts_engine.say(speech)
        tts_engine.runAndWait()
        tts_engine.stop()
        