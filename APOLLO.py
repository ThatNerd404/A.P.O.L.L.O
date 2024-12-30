from Settings import *

class Apollo():
    def __init__(self):
        self.app_is_running = True
        self.speak(f"Hello, I am APOLLO! I am your voice assistant! Ask away!")
        
        
    def run(self):
        while self.app_is_running:
            
                self.listen()
            
                if self.user_voice.lower().strip() in deactivation_words:
                    self.speak("Powering Off")
                    break
                elif self.user_voice == "":
                    self.speak("Sorry, I didn't hear you.")
                
                else:
                    self.speak(f"User said:{self.user_voice}")
                    self.speech_sentiment = sentiment_analysis(self.user_voice)[0]["label"]
                    if self.speech_sentiment == "POSITIVE":
                        self.speak("And that's very positive!")
                        
                    elif self.speech_sentiment == "NEGATIVE":
                        self.speak("And that's pretty negative!")
                
    def math(self):
        pass
    
    def listen(self):
        with sr.Microphone() as source:
            self.speak("Listening...")
            
            audio_recognizer.adjust_for_ambient_noise(source,0.5)
            self.audio = audio_recognizer.listen(source, timeout=10)
        
            try:
                self.user_voice = audio_recognizer.recognize_whisper(self.audio) #? uses whisper which doesnt need internet to work and is really accurate
    
            except sr.WaitTimeoutError:
                print("Timeout. Try speaking again.")
                
    def speak(self, speech):
        print(speech)
        tts_engine.say(speech)
        tts_engine.runAndWait()
        tts_engine.stop()
        