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

# Text-to-Speech Initialization
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  # Female voice
tts_engine.setProperty('volume', 1.0)

# Embedding Model and FAISS Setup
embedding_model = "all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

# Load and Split Documents


def load_documents(directory):
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


# Load documents and initialize the vector store
# Replace with your document folder path
documents = load_documents("Documents")
vector_store = create_faiss_store(documents)

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

# Apollo Class


class Apollo:
    def __init__(self):
        self.convo_history = ""
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model="phi3:3.8b")
        self.vector_store = vector_store
        self.chain = self.prompt | self.model

    def get_relevant_context(self, query):

        results = self.vector_store.similarity_search_with_score(query, k=3)
        relevant_docs = []
        threshold = 3
        for result, score in results:
            print(score)
            if score > threshold:
                relevant_docs.append(result.page_content)
            else:
                relevant_docs = []

        return relevant_docs

    def call_ai(self, user_prompt):
        if user_prompt == "quit":
            sys.exit()

        self.start_time = time.time()

        # Fetch relevant context from FAISS
        relevant_documents = self.get_relevant_context(user_prompt)

        # Generate response
        self.result = self.chain.invoke({
            "context": context,
            "documents": relevant_documents,
            "personality": personality,
            "convo_history": self.convo_history,
            "question": user_prompt
        })

        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time

        print(f"A.P.O.L.L.O: {self.result}")
        print(f"Answer took about: {self.total_time} seconds!")
        self.speak(self.result)

    def speak(self, speech):
        tts_engine.say(speech)
        tts_engine.runAndWait()
        tts_engine.stop()

    def run(self):
        print("Hello! I am A.P.O.L.L.O (Automated Personalized Operations for Learning and Life Organization).")
        print("Ask me anything, and I'll answer to the best of my ability. Type 'quit' to exit.")
        while True:
            user_input = input("User: ")
            self.call_ai(user_input)
            self.convo_history += f"\nUser: {user_input}\nApollo: {self.result}"


if __name__ == "__main__":
    ap = Apollo()
    ap.run()
