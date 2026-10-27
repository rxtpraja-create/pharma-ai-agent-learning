
import os
from getpass import getpass
from google import genai

print("=== Pharma AI Agent ===")
print("Your pharmaceutical learning assistant\n")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = getpass("Enter your Gemini API key: ")

client = genai.Client(api_key=api_key)

question = input("Ask a pharma question: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=(
        "You are a pharmaceutical learning assistant. "
        "Answer in simple Hinglish when appropriate. "
        "Explain GMP and pharmaceutical concepts accurately. "
        "Do not invent regulations or replace approved SOPs.\n\n"
        + question
    ),
)

print("\n=== AI Agent Answer ===\n")
print(response.text)
