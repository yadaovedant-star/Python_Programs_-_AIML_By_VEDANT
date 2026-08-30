from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env
load_dotenv()

# Initialize the Groq chat model
model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

# Create the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{user_input}")
])

print("AI Chatbot Started!")
print("Type 'exit' to quit.\n")

# Continuous chat loop
while True:

    # Take input from the user
    user_input = input("You: ")

    # Exit condition
    if user_input.lower().strip() == "exit":
        print("Goodbye!")
        break

    # Format the prompt
    formatted_prompt = prompt.format_messages(
        user_input=user_input
    )

    try:
        # Send prompt to the model
        response = model.invoke(formatted_prompt)

        # Print the response
        print("AI:", response.content)
        print()

    except Exception as e:
        # Handle errors
        print("Error:", e)
        print()