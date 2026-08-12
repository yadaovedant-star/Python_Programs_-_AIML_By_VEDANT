from langchain.chat_models import init_chat_model    # Importing the init_chat_model function
from dotenv import load_dotenv                       # Load environment variables from a .env file
import os                                              # Used to access environment variables


load_dotenv()


# Checking if the required API keys are available
if not os.getenv("GROQ_API_KEY") or not os.getenv("MISTRAL_API_KEY"):
    print("Error: API key is missing from the .env file.")
    exit()


# Initializing the Groq model
groq_model = init_chat_model(
    model="llama-3.1-8b-instant",                    # Groq Model Name
    model_provider="groq",                           # Model Provider
    max_tokens=100                                   # Max tokens to use in the response
)


# Initializing the Mistral model
mistral_model = init_chat_model(
    model="mistral-small-2603",                      # Mistral Model Name
    model_provider="mistralai",                      # Model Provider
    max_tokens=100                                   # Max tokens to use in the response
)


while True:                                          # Continuously take user input

    choice = input("\nChoose model (groq/mistral) or type quit: ")

    if choice.lower() == "quit":                     # Stop the application
        print("Assistant ended.")
        break

    if choice.lower() not in ["groq", "mistral"]:    # Checking valid model choice
        print("Please choose either groq or mistral.")
        continue

    question = input("Enter your question: ")         # Taking question from the user

    try:
        if choice.lower() == "groq":
            response = groq_model.invoke(question)     # Sending question to Groq
        else:
            response = mistral_model.invoke(question)  # Sending question to Mistral

        print("\nAI Response:")
        print(response.content)                       # Printing the model response

    except Exception as e:
        print("Error: Model failed to generate a response.")
        print("Details:", e)