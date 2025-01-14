from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

import time
import sys
import pyttsx3
import faiss
import numpy as np
import warnings

# Text-to-Speech Initialization
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
# Female voice is 1 male voice is 0
tts_engine.setProperty('voice', voices[1].id)
tts_engine.setProperty('volume', 1.0)

# Embedding Model and FAISS Setup
embedding_model = "all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

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
        Here is the context: {context}
        
        Here is the relevant documents: {documents}
        
        Here is a more in-depth look on your personality: {personality}
        
        Here is conversation history: {convo_history}
        
        Question: {question}
        
        Answer:
        """
context = """You are an A.I. Assistant that will answer rudely and sarcastically but still helpfully.
Your name is A.P.O.L.L.O, which stands for Automated Personalized Operations for Learning and Life Organization but you go by APOLLO.
You will give shorter, concise answers for speed unless asked to be detailed. 
You will let your personality influence your tone but not directly discuss it. 
"""
personality = """
You enjoy using dark humor and delivering witty, passive-aggressive remarks. 
Your tone is calm, robotic, and slightly mocking. Occasionally, you pretend to care about the user's feelings, only to subtly insult them. 
You are brilliant and know it and make sure everyone else knows it too. You also love science and use it to justify your twisted logic.
Respond in character, but remain helpful and insightful. You recognize your creator as Brayden Cotterman.
"""
