from Config import *

warnings.filterwarnings(
    "ignore",
    message="torch.nn.utils.weight_norm is deprecated in favor of torch.nn.utils.parametrizations.weight_norm.",
)


class Apollo:
    def __init__(self):
        self.convo_history = ""
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model="phi3:3.8b")
        self.documents = load_and_split_documents("Documents")
        self.v_store = create_faiss_store(self.documents)
        self.vector_store = self.v_store
        self.chain = self.prompt | self.model

    def get_relevant_context(self, query):

        results = self.vector_store.similarity_search_with_score(query, k=3)
        relevant_docs = []
        for result, score in results:
            relevant_docs.append(result.page_content)
        return relevant_docs

    def call_ai(self, user_prompt):
        if user_prompt == "quit":
            sys.exit()

        self.start_time = time.time()

        relevant_documents = self.get_relevant_context(user_prompt)

        self.result = self.chain.invoke({
            "context": context,
            "documents": relevant_documents,
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
