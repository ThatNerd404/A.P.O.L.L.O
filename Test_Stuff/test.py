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
    import os
    import subprocess
    import huggingface_hub
    
# Kill a process by name
    ollama_server = subprocess.Popen(    ["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    #os.system("taskkill /f /im ollama.exe")  # Replace with the process name
    os.system("taskkill /F /IM ollama.exe > nul 2>&1") 
# Kill a process by PID
    #os.system("taskkill /f /pid 1234")  # Replace with the process ID
    

    # Test the voice
    #engine.say("Hello, I am a British male voice. How can I assist you today?")
    #engine.runAndWait()
