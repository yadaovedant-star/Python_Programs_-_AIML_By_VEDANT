from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load the same embedding model used when creating the database
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load the existing Chroma database
vectorstore = Chroma(
    persist_directory="chroma-db",
    embedding_function=embeddings
)

# Create a retriever using MMR search
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2
    }
)

# Take a question from the user
question = input("Ask a question about Google: ")

# Retrieve relevant chunks
retrieved_documents = retriever.invoke(question)

# Print the retrieved documents
print("\n========== Retrieved Documents ==========\n")

for i, document in enumerate(retrieved_documents, start=1):
    print(f"--- Retrieved Chunk {i} ---")
    print(document.page_content)
    print()