import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_question(question):
    if not question.strip():
        return "Please enter a question."

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Answer this question clearly and simply for a college student:\n\n" + question
    )

    return response.text