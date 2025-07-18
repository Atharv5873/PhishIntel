from fastapi import FastAPI
from app.routes import detect

app = FastAPI(title="Gemini Guard – AI Phishing Detector")

app.include_router(detect.router)
