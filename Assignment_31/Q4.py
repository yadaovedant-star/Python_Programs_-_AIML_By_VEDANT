from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Hugging Face API model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7,
)

# Convert to chat model
chat_model = ChatHuggingFace(llm=llm)

# Create ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a very polite and helpful AI assistant."),
    ("human", "{user_input}")
])

# Take input from the user
user_input = input("Enter your question: ")

# Format the prompt
formatted_prompt = prompt.format_messages(
    user_input=user_input
)

# Send formatted prompt to the model
response = chat_model.invoke(formatted_prompt)

# Print response
print("\nAI Response:")
print(response.content)