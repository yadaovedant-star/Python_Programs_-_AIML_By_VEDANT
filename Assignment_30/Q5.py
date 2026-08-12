from langchain.chat_models import init_chat_model     # Importing the init_chat_model function from the langchain.chat_models module
from dotenv import load_dotenv        # Load environment variables from a .env file

load_dotenv()

model = init_chat_model(                     # Model From Mistral provider
    model="mistral-small-2603",        # Model Name
    model_provider="mistralai"      # Model Provider is mistralai
)

response = model.invoke(
    "Explain what is Artificial Intelligence in simple words."           # Question & instructions to the model
)

print(response.content)