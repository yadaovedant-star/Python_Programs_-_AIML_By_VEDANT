from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader
)

# Load PDF file
pdf_loader = PyPDFLoader("data/sample.pdf")
pdf_documents = pdf_loader.load()

# Print number of PDF pages
print("Number of PDF pages loaded:", len(pdf_documents))


# Load Wikipedia page
web_loader = WebBaseLoader(
    "https://en.wikipedia.org/wiki/Artificial_intelligence"
)

web_documents = web_loader.load()

# Print number of web documents
print("Number of Wikipedia documents loaded:", len(web_documents))