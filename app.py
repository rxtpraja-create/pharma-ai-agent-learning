import os
from getpass import getpass
from google import genai

print("=== Pharma AI Agent ===")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = getpass("Enter your Gemini API key: ")

client = genai.Client(api_key=api_key)

while True:
    question = input(
        "\nAsk a pharma question (or type exit): "
    ).strip()

    if question.lower() == "exit":
        print("Session ended.")
        break

    if not question:
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=(
                "You are a pharmaceutical learning assistant. "
                "Answer in simple Hinglish when appropriate. "
                "Explain GMP, QA, QMS, CAPA, deviations and "
                "data integrity accurately. Do not invent "
                "regulations or replace approved SOPs.\n\n"
                + question
            ),
        )
        print("\n=== Pharma AI Agent Answer ===\n")
        print(response.text)

    except Exception as e:
        print("Request failed:", type(e).__name__, str(e)[:500])
