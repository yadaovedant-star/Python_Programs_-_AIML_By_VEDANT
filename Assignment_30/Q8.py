from langchain.chat_models import init_chat_model    # Importing the init_chat_model function
from dotenv import load_dotenv                       # Load environment variables from a .env file


load_dotenv()


model = init_chat_model(                              # Initializing the Groq model
    model="llama-3.1-8b-instant",                    # Model Name
    model_provider="groq",                           # Model Provider
    max_tokens=100                                   # Max tokens to use in the response
)


while True:                                          # Continuously take user input

    user_input = input("You: ")                      # Taking input from the user in terminal

    if user_input.lower() == "exit":                 # Checking if the user wants to exit
        print("Chat ended.")
        break                                        # Exit the loop

    response = model.invoke(user_input)              # Sending user input to the Groq model

    print("AI:", response.content)                    # Printing the model's response