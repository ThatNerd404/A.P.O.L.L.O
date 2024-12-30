import pyttsx3
import speech_recognition as sr 
from transformers import pipeline 

sentiment_analysis = pipeline("sentiment-analysis")
tts_engine = pyttsx3.init()
audio_recognizer = sr.Recognizer()
audio_recognizer.energy_threshold = 200
audio_recognizer.pause_threshold = 1.0
audio_recognizer.dynamic_energy_threshold = True
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice',voices[0].id) #? sets voice to gender 0 for male 1 for female
tts_engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)
deactivation_words = ["quit.","quit", "quit!", "quit?",
"deactivate.", "deactivate", "deactivate!", "deactivate?",
"cancel.", "cancel", "cancel!", "cancel?"]
        