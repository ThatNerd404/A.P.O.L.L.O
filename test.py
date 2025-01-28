'''from sentence_transformers import SentenceTransformer
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
'''
from Config import *
class Apollo:
    def __init__(self):
        self.speak("Initializing Systems.")

        self.convo_history = ""
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model="llama3.2:1b")
        self.documents = load_and_split_documents("Documents")
        self.v_store = create_faiss_store(self.documents)
        self.vector_store = self.v_store
        self.chain = self.prompt | self.model

        self.speak("Initializing Complete.")

    def listen_for_wakeword(self, source):
        while True:
            audio = audio_recognizer.listen(source)
            try:
                user_audio = audio_recognizer.recognize_whisper(audio)
                if "apollo" in user_audio.lower():
                    print("Wake word detected!")
                    random_greeting = random.choice(Greetings)
                    self.speak(random_greeting)
                    self.listen_and_respond(source)
                    break

            except sr.UnknownValueError:
                pass

            except sr.WaitTimeoutError:
                pass

    def listen_and_respond(self, source):
        while True:
            try:
                audio = audio_recognizer.listen(source, timeout=5)
                user_audio = audio_recognizer.recognize_whisper(audio)
                print(f"Apollo heard: {user_audio}")

                if "quit" in user_audio.lower():
                    sys.exit()

                elif not user_audio:
                    print("Silence found, shutting up, listening for wake word ...")
                    self.listen_for_wakeword(source)

                elif not audio:
                    print("Silence found, shutting up, listening for wake word ...")
                    self.listen_for_wakeword(source)

                self.speak("Processing Request")
                Ai_response = self.call_ai(user_audio)
                print(Ai_response)
                self.speak(Ai_response)
                self.convo_history += f"User: {user_audio} Apollo: {Ai_response}"

            except sr.UnknownValueError:
                print("Silence found, shutting up, listening for wake word ...")
                self.listen_for_wakeword(source)
                break

            except sr.WaitTimeoutError:
                print("Silence found, shutting up, listening for wake word ...")
                self.listen_for_wakeword(source)
                break

    def get_relevant_context(self, query):

        # ? speed goes down the more k (the amount of chunks grabbed) goes up
        results = self.vector_store.similarity_search_with_score(query, k=3)
        relevant_docs = []
        for result, score in results:
            relevant_docs.append(result.page_content)
            print(score)
        return relevant_docs

    def call_ai(self, user_prompt):

        self.start_time = time.time()

        relevant_documents = self.get_relevant_context(user_prompt)
        try:
            result = self.chain.invoke({
                "context": context,
                "documents": relevant_documents,
                "convo_history": self.convo_history,
                "question": user_prompt
            })

        except Exception as e:
            print(f"Error: {e}")
            result = f"It seems an error has occured in formulating a response. Perhaps try ensuring Ollama is running?"

        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time

        print(f"Answer took about: {self.total_time} seconds!")
        return result

    def speak(self, speech):
        tts_engine.say(speech)
        tts_engine.runAndWait()
        tts_engine.stop()

    def run(self):
        while True:
            with sr.Microphone() as source:
                self.listen_for_wakeword(source)


if __name__ == "__main__":
    ap = Apollo()
    ap.run()

if __name__ == "__main__":
    import pyttsx4

    # Initialize the engine
    
    engine = pyttsx4.init()
    engine.say('this is an english text to voice test.')
    engine.runAndWait()
    

    # Test the voice
    #engine.say("Hello, I am a British male voice. How can I assist you today?")
    #engine.runAndWait()
