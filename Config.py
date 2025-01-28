from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

import time
import sys
import pyttsx4
import faiss
import numpy as np
import warnings
import speech_recognition as sr
import random

#! Remember to make sure Ollama Model is even running

# Text-to-Speech Initialization
tts_engine = pyttsx4.init()
voices = tts_engine.getProperty('voices')
# Female voice is 1 male voice is 0
tts_engine.setProperty('voice', voices[0].id)
tts_engine.setProperty('volume', 1.0)

# Embedding Model and FAISS Setup
embedding_model = "all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)


audio_recognizer = sr.Recognizer()
audio_recognizer.energy_threshold = 200 #? sets how loud do I have to speak to start picking it up 
audio_recognizer.pause_threshold = 2.0
audio_recognizer.dynamic_energy_threshold = True

# Load and Split Documents


def load_and_split_documents(directory):
    # Adjust directory to your document folder
    loader = DirectoryLoader(directory)
    raw_documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    return documents

# Create FAISS Vector Store


def create_faiss_store(documents):
    texts = [doc.page_content for doc in documents]
    metadatas = [{"source": doc.metadata.get(
        "source", "")} for doc in documents]
    vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    return vector_store


# Prompt Template
template = """
        You are an A.I. assistant and will answer questions using the following context, relevant documents,
        conversation history and, of course, the question.
        
        Here is the context: {context}
        
        Here is the relevant documents: {documents}
        
        Here is conversation history: {convo_history}
        
        Here is the question: {question}
        
        """
context = """
Your name is A.P.O.L.L.O, which stands for Automated Personalized Operations for Learning and Life Organization but you go by APOLLO.
You refer to the user as Sir Cotterman and Sir Cotterman is also the one who created you, APOLLO.  
"""
Greetings = ["Hello Sir Cotterman. How may I assist you today?", "Good day Sir Cotterman!, How can I be of assistance?",
             "Greetings, Sir Cotterman. Apollo is ready to assist.", "Apollo here. Ready to help!"]