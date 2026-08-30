from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Initialize LLM
model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing Chroma vector store
vectorstore = Chroma(
    persist_directory="chroma-db",
    embedding_function=embeddings
)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2}
)

# Create RAG prompt
rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Answer the question ONLY using the provided context.

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

# RAG function
def ask_question(question):
    retrieved_documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    formatted_prompt = rag_prompt.format_messages(
        context=context,
        question=question
    )

    response = model.invoke(formatted_prompt)

    return response.content

# Test with 3 questions
print("COMPLETE RAG APPLICATION")

for i in range(3):
    question = input(f"\nEnter question {i + 1}: ")

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)

print("\nRAG testing completed.")