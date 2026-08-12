from dotenv import load_dotenv
import os          # Imported the os module to access environment variables

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")        # Get the GROQ API key from environment variables
mistral_key = os.getenv("MISTRAL_API_KEY")  # Get the MISTRAL API key from environment variables

if groq_key and mistral_key:          # Check if both API keys are present
    print("API keys loaded successfully.")
else:
    print("API keys are missing.")