import sys
import pyttsx3
import speech_recognition as sr 
from transformers import pipeline 
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice',voices[0].id) #? sets voice to gender 0 for male 1 for female
tts_engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)

audio_recognizer = sr.Recognizer()
audio_recognizer.energy_threshold = 200 #? sets how loud do I have to speak to start picking it up 
audio_recognizer.pause_threshold = 1.0
audio_recognizer.dynamic_energy_threshold = True


deactivation_words = ["quit.","quit", "quit!", "quit?",
"deactivate.", "deactivate", "deactivate!", "deactivate?",
"cancel.", "cancel", "cancel!", "cancel?"]

#sentiment_analysis = pipeline("sentiment-analysis", model="distilgpt2")
chatbot = pipeline(model="facebook/blenderbot-400M-distill")
#conversation = "What's up!"
#print(conversation)
#conversation =  chatbot(conversation)
#print(conversation)
#question_answering = pipeline("question-answering", model="distilgpt2")