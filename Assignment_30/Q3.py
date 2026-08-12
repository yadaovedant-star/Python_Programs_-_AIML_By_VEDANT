from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(                   # Using LLAMA Model 
    model="llama-3.1-8b-instant",
    model_provider="groq"      
)

response = model.invoke("Introduce yourself in 3 sentences.")           #Question Or instructions to the model

print(response.content)