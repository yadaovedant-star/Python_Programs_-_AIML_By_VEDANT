from langchain.chat_models import init_chat_model     # Importing the init_chat_model function from the langchain.chat_models module       
from dotenv import load_dotenv        # Load environment variables from a .env file 

load_dotenv()

model = init_chat_model(                         # Model with temperature 0.2
    model="llama-3.1-8b-instant",               # Model Name
    model_provider="groq",                      # Model Provider is groq
    temperature=0.2,                          # Temperature for randomness
    max_tokens=50                               # Max tokens to use in the response
)

response = model.invoke("Introduce yourself in 3 sentences.")         #Question Or instructions to the model

print(response.content)