from fastapi import FastAPI
from backend.models import PromptRequest

from backend.services.openai_service import call_openai
from backend.services.gemini_service import call_gemini
from backend.services.claude_service import call_claude

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LLM Comparison API is running"}

