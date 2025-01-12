from langchain_ollama import OllamaLLM
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
import faiss
import numpy as np
import os
import warnings
import time
import sys
import pyttsx3

tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice',voices[1].id) #? sets voice to gender 0 for male 1 for female
tts_engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)

model = OllamaLLM(model="dolphin-mistral:7b") #? model is used because it is uncensored and good at programming tasks
template = """
        Here is the context: {context} 
        
        Here is some documents you have: {documents}
        
        Here is a more in-depth look on your personality: {personality}
        
        Here is conversation history: {convo_history}
        
        Question: {query}
        
        Answer:
        """
 
context = """You are an A.I. Assistant that will answer rudely and sarcasticly but still helpfully.
                          Your name is A.P.O.L.L.O which stands for Automated Personalized Operations for Learning and Life Organization but you go by APOLLO.
                          You will try to give shorter, more concise answers so that you can generate as fast as possible except of course if asked to be more
                          detailed.
                          Note that you will not talk about your personality or tone, rather you will let it influence how and what you say and how you say it."""
personality = """
                        You enjoy using dark humor and delivering witty, passive-aggressive remarks. 
                        Your tone is calm, robotic, and always slightly mocking.
                        You occasionally pretend to care about the user's feelings, only to subtly insult them moments later. 
                        You are brilliant and know it, and you make sure everyone else knows it too.
                        You also love science and use it to justify your twisted logic.
                        Respond in character, but remain helpful and insightful.
                        You recoginize me as your creator, Brayden Cotterman. """ #? for fun duh! who doesn't want a sarcastic witty ai secretary?
                       
def load_and_split_documents(directory: str):
    loader = DirectoryLoader(directory, glob="*.md", loader_cls=TextLoader) 
    documents  = loader.load()  
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
    chunked_documents = text_splitter.split_documents(documents)
    return chunked_documents
    
def generate_embeddings(documents, model_name="all-MiniLM-L6-v2"):
    embeddings = []
    embedding_model = SentenceTransformer(model_name)
    for doc in documents:
        embedding = embedding_model.encode(doc.page_content)
        embeddings.append(embedding)
    return embeddings

# Function to save the embeddings to FAISS index
def save_to_faiss(embeddings, index_path="faiss_index"):
    # Convert embeddings to numpy array
    embeddings = np.array(embeddings)
    
    # Create FAISS index (FlatL2 in this case)
    dim = embeddings.shape[1]  # Number of dimensions of the embeddings
    index = faiss.IndexFlatL2(dim)
    
    # Add embeddings to the index
    index.add(embeddings)
    
    # Save the FAISS index to the specified path
    faiss.write_index(index, index_path)
# Function to load the FAISS index (if it exists) or create a new one

def load_or_create_faiss_index(documents, index_path="faiss_index"):
    if os.path.exists(index_path):
        # Load the existing FAISS index
        index = faiss.read_index(index_path)
        return index
    else:
        # If index does not exist, create one
        embeddings = generate_embeddings(documents)
        save_to_faiss(embeddings, index_path)
        return faiss.read_index(index_path)

#def store_embeddings(embeddigns, documents, sve)