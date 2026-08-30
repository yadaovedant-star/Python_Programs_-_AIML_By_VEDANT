from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the document from Q2
loader = TextLoader("data/company_info.txt")
documents = loader.load()

# Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Split the document into chunks
chunks = text_splitter.split_documents(documents)

# Print total number of chunks
print("Total number of chunks:", len(chunks))

# Display the first 3 chunks
for i, chunk in enumerate(chunks[:3], start=1):
    print(f"\n========== CHUNK {i} ==========\n")
    print(chunk.page_content)