from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import warnings
import time
import sys
import pyttsx3
warnings.filterwarnings(
    "ignore",
    message="torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.",
)

class Apollo():
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        voices = self.tts_engine.getProperty('voices')
        self.tts_engine.setProperty('voice',voices[1].id) #? sets voice to gender 0 for male 1 for female
        self.tts_engine.setProperty('volume',1.0) #? sets voice from 100 (1.0) to 1 (0.01)

        self.model = OllamaLLM(model="dolphin-mistral:7b") #? model is used because it is uncensored and good at programming tasks
        self.template = """
        Answer the question below.
        
        Here is the conversation history: {context}
        
        Question: {question}
        
        Answer:
        """
        self.prompt = ChatPromptTemplate.from_template(self.template)
        self.chain = self.prompt | self.model
        self.context = """You are a very sarcastic and rude ai.
        Your name is A.P.O.L.L.O which stands for Automated Personalized Operations for Learning and Life Organization but you go by APOLLO.
        You recoginize me as your creator, Brayden Cotterman. """ #? for fun duh! who doesn't want a sarcastic witty ai secretary?
    
    def run(self):
        print("Hello! I am A.P.O.L.L.O which stands for Automated Personalized Operations for Learning and Life Organization. Ask me anything and I will answer to the best of my ability.")
        while True:
            user_input = input("User: ")
            self.call_ai(user_input)
            self.context += f"\n User: {user_input}\nApollo:{self.result}"
    
    def call_ai(self,user_prompt):
        if user_prompt == "quit":
            sys.exit()
            
        self.start_time = time.time()
        self.result = self.chain.invoke({"context": self.context, "question" : user_prompt})
        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        
        print("A.P.O.L.L.O: ",self.result)
        print(f"Answer took about: {self.total_time} seconds!")
        self.speak(self.result)
        
    def speak(self,speech):
        self.tts_engine.say(speech)
        self.tts_engine.runAndWait()
        self.tts_engine.stop()
     
if __name__ == "__main__":
    ap = Apollo()
    ap.run()