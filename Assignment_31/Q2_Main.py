from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

# Model ID
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model locally
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Create text-generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
)

# Convert Hugging Face pipeline into LangChain LLM
llm = HuggingFacePipeline(pipeline=pipe)

# Convert it into a chat model
chat_model = ChatHuggingFace(llm=llm)

# Ask the model to introduce itself
response = chat_model.invoke("Introduce Yourself in 100 words")

# Print the complete response
print(response.content)