from Config import *

warnings.filterwarnings(
    "ignore",
    message="torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.",
)

class Apollo():
    def __init__(self):
        self.convo_history = ""
        directory = "Documents"
        documents = load_and_split_documents(directory)
        #print(documents[0])
        embeddings = generate_embeddings(documents)
        text_list = [doc.page_content for doc in documents]  # Create a list of (text, embedding) tuples
        text_embedding_pairs = list(zip(text_list, embeddings))
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.retriever = FAISS.from_embeddings(text_embeddings= text_embedding_pairs, embedding=self.embedding_model)
        prompt = PromptTemplate(input_variables=["context","documents", "personality", "convo_history", "query"], template=template)
        self.qa_chain = RetrievalQA.from_chain_type(
        llm=model, 
        chain_type="stuff",  # Use "stuff" to stuff the documents directly into the prompt
        retriever= self.retriever.as_retriever(),
        return_source_documents=False,  # Optional: retrieve source documents as well
        chain_type_kwargs={"prompt": prompt},
)
        #self.qa_chain.prompts["question"] = prompt
        
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
        self.result = self.qa_chain.invoke({"context":context, "documents": self.retriever, "personality": personality, "convo_history": self.convo_history,"query":user_prompt})
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