import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_text(text):
    if not text.strip():
        return "Please enter content to summarize."

    return (
        "EduGenie Summary:\n\n"
        "This is a simple summary of the given content:\n\n"
        + text
    )