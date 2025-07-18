# 🛡️ Gemini Guard – AI Phishing Detector

Gemini Guard is a real-time phishing detection API built with **FastAPI**, **MongoDB**, and **Gemini AI**. Paste suspicious emails, messages, or links, and let AI detect if it's phishing — with human-style explanations.

##  Tech Stack

- 🚀 FastAPI (Python)
- 📦 MongoDB Atlas (Motor async)
- 🤖 Gemini Pro API (Google Generative AI)
- 🔐 dotenv for secrets

##  Features

- `/detect`: Analyze content for phishing signs
- AI-generated explanations (verdict + reasoning + suggestions)
- MongoDB logs for analytics and feedback
- Ready for deployment on Render/Railway

##  Sample Usage

```bash
curl -X POST http://localhost:8000/detect \
-H "Content-Type: application/json" \
-d '{"content": "Your account is suspended. Click here: http://phishy.link"}'
```

