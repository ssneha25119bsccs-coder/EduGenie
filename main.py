from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path
from fastapi.responses import HTMLResponse
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="EduGenie")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "templates" / "index.html"

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_FILE.read_text(encoding="utf-8")

@app.get("/qa")
def question_answer(question: str):
    return {"answer": answer_question(question)}

@app.get("/explain")
def explain(text: str):
    return {"answer": explain_topic(text)}

@app.get("/quiz")
def quiz(topic: str):
    return {"quiz": generate_quiz(topic)}

@app.get("/summarize")
def summarize(text: str):
    return {"summary": summarize_text(text)}

@app.get("/learn/recommendations")
def recommendations(topic: str):
    return {"recommendations": recommend_learning_path(topic)}