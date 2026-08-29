import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFacePipeline,
    ChatHuggingFace,
)

# Load environment variables
load_dotenv()

question = "What is the difference between AI and Machine Learning?"

# ---------------- API MODEL ----------------

api_llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7,
)

api_chat = ChatHuggingFace(llm=api_llm)

api_response = api_chat.invoke(question)


# ---------------- LOCAL MODEL ----------------

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
)

local_llm = HuggingFacePipeline(pipeline=pipe)

local_chat = ChatHuggingFace(llm=local_llm)

local_response = local_chat.invoke(question)


# ---------------- PRINT RESPONSES ----------------

print("\n========== API Model Response ==========\n")
print(api_response.content)

print("\n========== Local Model Response ==========\n")
print(local_response.content)


# ---------------- OBSERVATION ----------------

print("\n========== Observation ==========\n")
print(
    "The API model generally provides a more detailed and accurate response "
    "because DeepSeek-R1 is a much larger and more capable model. The local "
    "TinyLlama model runs on the computer without requiring an API, but its "
    "response quality may be lower. The local model can also be faster after "
    "the model has been downloaded, depending on the computer's hardware."
)