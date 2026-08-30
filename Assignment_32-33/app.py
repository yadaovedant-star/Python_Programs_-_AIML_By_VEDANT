import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Check for Groq API key
if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY is missing from .env")
    exit()

# Initialize the Groq chat model
model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

# Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load the existing Chroma database
vectorstore = Chroma(
    persist_directory="chroma-db",
    embedding_function=embeddings
)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2}
)

# Create system prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful Google information assistant.

Answer the user's question ONLY using the provided knowledge base.

If the answer is not present in the knowledge base,
say exactly:
"I could not find the answer."

Do not use outside knowledge.

Knowledge Base:
{context}
"""
    ),
    (
        "human",
        "{question}"
    )
])

print("Google RAG Chatbot")
print("Ask questions about the knowledge base.")
print("Type 'exit' to quit.\n")

# Continuous chat loop
while True:

    question = input("You: ").strip()

    # Exit condition
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Handle empty input
    if not question:
        print("Please enter a question.\n")
        continue

    try:
        # Retrieve relevant documents
        retrieved_documents = retriever.invoke(question)

        # Combine retrieved chunks into context
        context = "\n\n".join(
            document.page_content
            for document in retrieved_documents
        )

        # Format the RAG prompt
        formatted_prompt = prompt.format_messages(
            context=context,
            question=question
        )

        # Generate answer
        response = model.invoke(formatted_prompt)

        # Print answer
        print("\nAI:", response.content)
        print()

    except Exception as e:
        print("\nError:", e)
        print()