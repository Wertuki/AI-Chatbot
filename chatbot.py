import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def chat_with_ai(prompt):
    """AI-powered chatbot using OpenAI GPT-4."""
    openai.api_key = API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=150
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_ai(user_input)
        print("AI:", response)
