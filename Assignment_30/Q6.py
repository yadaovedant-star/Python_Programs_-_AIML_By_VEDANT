from langchain.chat_models import init_chat_model  # Importing the init_chat_model function from the langchain.chat_models module
from dotenv import load_dotenv       # Load environment variables from a .env file

load_dotenv()       

groq_model = init_chat_model(           # Model For Groq provider       
    model="llama-3.1-8b-instant",          # Model Name
    model_provider="groq",                # Model Provider is groq
    max_tokens=100                      # Max tokens to use in the response
)

mistral_model = init_chat_model(       # Model For Mistral provider
    model="mistral-small-2603",
    model_provider="mistralai",
    max_tokens=100
)

question = "What are the advantages of using LangChain?"             # Question saved in an Question variable

groq_response = groq_model.invoke(question)           #Response from Groq model
mistral_response = mistral_model.invoke(question)       #Response from Mistral model

print("Groq Response:")          # printing the response from Groq model
print(groq_response.content)

print("\nMistral Response:")        # printing the response from Mistral model
print(mistral_response.content)