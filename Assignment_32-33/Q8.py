from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# Load the same embedding model used for the Chroma database
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load the existing Chroma database
vectorstore = Chroma(
    persist_directory="chroma-db",
    embedding_function=embeddings
)

# Create MMR retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2}
)

# Create the RAG prompt template
rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not found in the context, say exactly:
"I could not find the answer."

Do not use outside knowledge.

Context:
{context}
"""
    ),
    (
        "human",
        "{question}"
    )
])

# Take question from the user
question = input("Ask a question about Google: ")

# Retrieve relevant documents
retrieved_documents = retriever.invoke(question)

# Combine retrieved chunks into context
context = "\n\n".join(
    document.page_content
    for document in retrieved_documents
)

# Pass context and question into the prompt
formatted_prompt = rag_prompt.format_messages(
    context=context,
    question=question
)

# Print the formatted prompt
print("\n========== Formatted RAG Prompt ==========\n")
print(formatted_prompt)