from Config import *

class Apollo:
    def __init__(self):
        self.convo_history = ""
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model="llama3.2:1b")
        self.documents = load_and_split_documents("Documents")
        self.v_store = create_faiss_store(self.documents)
        self.vector_store = self.v_store
        self.chain = self.prompt | self.model

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

    def test(self):
        while True:
            user_input = input("Ask the ai sumn:")
            if user_input == "quit":
                sys.exit()
            Ai_response = self.call_ai(user_input)
            print(Ai_response)
            

if __name__ == "__main__":
    ap = Apollo()
    ap.test()
