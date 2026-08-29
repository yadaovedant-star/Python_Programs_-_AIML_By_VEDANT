from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Load environment variables from .env
load_dotenv()

# Create Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
)

# Convert the LLM into a chat model
chat_model = ChatHuggingFace(llm=llm)

# Ask the model to introduce itself
response = chat_model.invoke(
    "Introduce yourself briefly."
)

# Print the response
print(response.content)