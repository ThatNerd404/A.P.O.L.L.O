from Config import *

warnings.filterwarnings(
    "ignore",
    message="torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.",
)

class Apollo():
    def __init__(self):
        self.convo_history = ""
        self.prompt = ChatPromptTemplate.from_template(template)
        self.chain = self.prompt | model
        
    def run(self):
        print("Hello! I am A.P.O.L.L.O which stands for Automated Personalized Operations for Learning and Life Organization. Ask me anything and I will answer to the best of my ability.")
        while True:
            user_input = input("User: ")
            self.call_ai(user_input)
            self.convo_history += f"\n User: {user_input}\nApollo:{self.result}"
    
    def call_ai(self,user_prompt):
        if user_prompt == "quit":
            sys.exit()
            
        self.start_time = time.time()
        self.result = self.chain.invoke({"context":context,"personality": personality, "convo_history": self.convo_history, "question" : user_prompt})
        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        
        print("A.P.O.L.L.O: ",self.result)
        print(f"Answer took about: {self.total_time} seconds!")
        self.speak(self.result)
        
    def speak(self,speech):
        tts_engine.say(speech)
        tts_engine.runAndWait()
        tts_engine.stop()
     
if __name__ == "__main__":
    ap = Apollo()
    ap.run()