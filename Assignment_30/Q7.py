from langchain.chat_models import init_chat_model    # Importing the init_chat_model function from the langchain.chat_models module
from dotenv import load_dotenv                # Load environment variables from a .env file

load_dotenv()

prompt = "Write a short creative story about a robot learning to cook."

model_01 = init_chat_model(                  # Model with temperature 0.1
    model="llama-3.1-8b-instant",            # Model Name
    model_provider="groq",                   # Model Provider we can use any provider like mistralai, groq, etc.      
    temperature=0.1,                         # Temperature value
    max_tokens=100                           # Max tokens to use in the response
)

model_07 = init_chat_model(                 # Model with temperature 0.7
    model="llama-3.1-8b-instant", 
    model_provider="groq",
    temperature=0.7,
    max_tokens=100
)

model_12 = init_chat_model(                 # Model with temperature 1.2 
    model="llama-3.1-8b-instant",
    model_provider="groq",
    temperature=1.2,
    max_tokens=100
)

response_01 = model_01.invoke(prompt)           #Response from model with temperature 0.1
response_07 = model_07.invoke(prompt)           #Response from model with temperature 0.7
response_12 = model_12.invoke(prompt)           #Response from model with temperature 1.2

print("Temperature = 0.1")
print(response_01.content)                      #printing the response from model with temperature 0.1

print("\nTemperature = 0.7")                    #printing the response from model with temperature 0.7
print(response_07.content)

print("\nTemperature = 1.2")                    #printing the response from model with temperature 1.2
print(response_12.content)