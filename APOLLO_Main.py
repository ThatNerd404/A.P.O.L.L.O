from Config import *

warnings.filterwarnings(
    "ignore",
    message="torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.",
)


class Apollo:
    def __init__(self):
        self.speak("Initializing Systems.")
        
        self.convo_history = ""
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model="phi3:3.8b")
        self.documents = load_and_split_documents("Documents")
        self.v_store = create_faiss_store(self.documents)
        self.vector_store = self.v_store
        self.chain = self.prompt | self.model
        
        self.speak("Initializing Complete.")
        
    def listen_for_wakeword(self, source):
        while True:
            audio =  audio_recognizer.listen(source)
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
            
    def listen_and_respond(self,source):
        while True:
            
            try:
                audio = audio_recognizer.listen(source, timeout=5)
                print("Listening...")
                user_audio = audio_recognizer.recognize_whisper(audio)
                print(f"Apollo heard {user_audio}")
                
                if "quit" in user_audio:
                    sys.exit()
                
                elif not user_audio:
                    continue
                
                if user_audio == "" or user_audio == None:
                    print("Silence found, shutting up, listening for wake word ...")
                    self.listen_for_wakeword(source)
                
                Ai_response = self.call_ai(user_audio)
                print(Ai_response)
                self.speak(Ai_response)
                
            except sr.UnknownValueError:
                print("Silence found, shutting up, listening for wake word ...")
                self.listen_for_wakeword(source)
                
            except sr.WaitTimeoutError:
                print("Silence found, shutting up, listening for wake word ...")
                self.listen_for_wakeword(source)
                break
        
    def get_relevant_context(self, query):

        results = self.vector_store.similarity_search_with_score(query, k=1)
        relevant_docs = []
        for result, score in results:
            relevant_docs.append(result.page_content)
        return relevant_docs

    def call_ai(self, user_prompt):

        self.start_time = time.time()

        relevant_documents = self.get_relevant_context(user_prompt)

        result = self.chain.invoke({
            "context": context,
            "documents": relevant_documents,
            "convo_history": self.convo_history,
            "question": user_prompt
        })

        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        
        print(f"Answer took about: {self.total_time} seconds!")
        return result

    def speak(self, speech):
        tts_engine.say(speech)
        tts_engine.runAndWait()
        tts_engine.stop()

    def run(self):
        print("Hello! I am A.P.O.L.L.O (Automated Personalized Operations for Learning and Life Organization).")
        print("Ask me anything, and I'll answer to the best of my ability. Type 'quit' to exit.")
        
        while True:
            with sr.Microphone() as source:
                self.listen_for_wakeword(source)
            
            

if __name__ == "__main__":
    ap = Apollo()
    ap.run()
