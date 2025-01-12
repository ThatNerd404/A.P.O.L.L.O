from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
import os

# Initialize the Ollama LLM model
model = OllamaLLM(model="dolphin-mistral:7b")

# Step 1: Load documents
loader = DirectoryLoader("Documents/", glob="*.md")
documents = loader.load()

# Step 2: Create embeddings and vectorstore
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
chroma_db_path = "chroma_db"
if not os.path.exists(chroma_db_path):
    # If the Chroma vectorstore doesn't exist, create it
    vectorstore = Chroma.from_documents(documents, embedding=embeddings.embed, persist_directory=chroma_db_path)
    vectorstore.persist()  # Save the vectorstore to disk
else:
    # If the Chroma vectorstore exists, load it
    vectorstore = Chroma(persist_directory=chroma_db_path, embedding_function=embeddings)

# Step 3: Setup the retrieval-based tool
retrieval_chain = RetrievalQA.from_chain_type(
    llm=model,
    retriever=vectorstore.as_retriever()
)
retrieval_tool = Tool(
    name="Document Retrieval",
    func=retrieval_chain.run,
    description="Use this tool to answer questions based on your uploaded documents."
)

# Step 4: Setup the general chat LLM
chat_llm = model  # Replace with a local model if needed

# Step 5: Initialize the agent
agent = initialize_agent(
    tools=[retrieval_tool],
    llm=chat_llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Step 6: Chatbot loop
print("AI Agent is ready! Type 'exit' to quit.\n")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    
    response = agent.invoke(query)
    print(f"AI Agent: {response}\n")
