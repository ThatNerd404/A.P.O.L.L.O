'''from Config import *

class Apollo:
    def __init__(self):
       # Start Ollama server in the background
        self.ollama_process = subprocess.Popen(
            ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        
    def call_ai(self, user_prompt):

        self.start_time = time.time()

        relevant_documents = self.get_relevant_context(user_prompt)
        try:
            result = self.chain.invoke({
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

'''
'''if __name__ == "__main__":
    ap = Apollo()
    ap.run()
'''
if __name__ == "__main__":
    import datetime 
    from pathlib import Path
    convo_history_directory = Path("C:\\Users\\MyCom\Desktop\\.vscode\\Github_Projects\\A.P.O.L.L.O\\Conversations")
    current_time = datetime.datetime.now()
    current_day = current_time.day
    convo_file = convo_history_directory / f"Chat_History_{str(current_day)}"
    with open(convo_file, "w") as cf:
        cf.write("Penis Fart 2")
    

    # Test the voice
    #engine.say("Hello, I am a British male voice. How can I assist you today?")
    #engine.runAndWait()
