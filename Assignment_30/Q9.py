from langchain.chat_models import init_chat_model    # Importing the init_chat_model function
from dotenv import load_dotenv                       # Load environment variables from a .env file


load_dotenv()


model = init_chat_model(                              # Initializing the Groq model
    model="llama-3.1-8b-instant",                    # Model Name
    model_provider="groq",                           # Model Provider
    max_tokens=200                                   # Max tokens to use in the response
)


def explain_topic(topic):                             # Function that takes a topic as input

    prompt = f"""
Explain the following topic: {topic}

Provide the answer in this structure:

1. Short Definition:
Give a short and simple definition.

2. Three Key Points:
- Key Point 1
- Key Point 2
- Key Point 3

3. Real-Life Example:
Give one simple real-life example.
"""

    response = model.invoke(prompt)                   # Sending the structured prompt to the Groq model

    print(response.content)                           # Printing the model's response


explain_topic("Machine Learning")                      # Testing the function with Machine Learning