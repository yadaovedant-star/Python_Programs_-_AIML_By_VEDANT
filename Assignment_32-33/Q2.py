from langchain_community.document_loaders import TextLoader

# Load the company information text file
loader = TextLoader("data/company_info.txt")

# Load the document
documents = loader.load()

# Print the number of documents loaded
print("Number of documents loaded:", len(documents))

# Print the content of the first document
print("\nFirst Document Content:")
print(documents[0].page_content)