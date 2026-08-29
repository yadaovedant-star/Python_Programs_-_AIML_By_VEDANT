import os
from dotenv import load_dotenv

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFacePipeline,
    ChatHuggingFace,
)

from langchain_core.prompts import ChatPromptTemplate


# ============================================================
# Load environment variables from .env
# ============================================================

load_dotenv()


# ============================================================
# System prompt
# ============================================================

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a very polite and helpful AI assistant."
    ),
    (
        "human",
        "{user_input}"
    )
])


# ============================================================
# API MODE - HuggingFaceEndpoint
# ============================================================

def create_api_model():

    # Check whether Hugging Face API token exists
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not token:
        raise ValueError(
            "Hugging Face API token is missing. "
            "Please add HUGGINGFACEHUB_API_TOKEN to your .env file."
        )

    # Create Hugging Face API endpoint
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",
        task="text-generation",
        max_new_tokens=200,
        temperature=0.7,
    )

    # Convert LLM into chat model
    return ChatHuggingFace(llm=llm)


# ============================================================
# LOCAL MODE - HuggingFacePipeline
# ============================================================

def create_local_model():

    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    print("\nLoading local TinyLlama model...")
    print("Please wait...\n")

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    # Load local model
    model = AutoModelForCausalLM.from_pretrained(model_id)

    # Create text-generation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=200,
    )

    # Convert pipeline into LangChain LLM
    llm = HuggingFacePipeline(
        pipeline=pipe
    )

    # Convert LLM into chat model
    return ChatHuggingFace(llm=llm)


# ============================================================
# Select chatbot mode
# ============================================================

print("========================================")
print("       DUAL MODE AI CHATBOT")
print("========================================")
print("1. Hugging Face API Mode")
print("2. Local Hugging Face Mode")
print("========================================")

mode = input("Choose a mode (1/2): ").strip()


# ============================================================
# Create selected model
# ============================================================

try:

    if mode == "1":

        print("\nStarting Hugging Face API Mode...\n")
        chat_model = create_api_model()

    elif mode == "2":

        print("\nStarting Local Hugging Face Mode...")
        chat_model = create_local_model()

    else:

        print("\nInvalid choice. Please select 1 or 2.")
        exit()


except Exception as e:

    print("\nError while loading the model:")
    print(e)
    exit()


# ============================================================
# Chat loop
# ============================================================

print("========================================")
print("Chatbot started!")
print("Type 'exit' to quit.")
print("========================================\n")


while True:

    try:

        # Take input from user
        user_input = input("You: ")

        # Exit condition
        if user_input.lower().strip() == "exit":
            print("\nGoodbye! ")
            break

        # Ignore empty input
        if not user_input.strip():
            print("Please enter a message.")
            continue

        # Format the ChatPromptTemplate
        formatted_prompt = prompt.format_messages(
            user_input=user_input
        )

        # Send prompt to selected model
        response = chat_model.invoke(formatted_prompt)

        # Print response
        print("\nAI:", response.content)
        print()

    except Exception as e:

        # Handle errors without crashing the chatbot
        print("\nError:", e)
        print("Please try again.\n")