import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load the document
loader = TextLoader("data/company_info.txt")
documents = loader.load()

print("Documents loaded:", len(documents))

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Chunks created:", len(chunks))

# Create Hugging Face embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store the chunks in Chroma
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma-db"
)

# Confirm that the database was created
if os.path.exists("chroma-db"):
    print("Chroma database created successfully!")
else:
    print("Chroma database creation failed.")