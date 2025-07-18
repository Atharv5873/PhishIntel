from fastapi import APIRouter, HTTPException
from app.models.phishing import DetectRequest, DetectResponse
from app.services.gemini import analyze_content
from app.db.mongo import detections
from datetime import datetime


router=APIRouter()

@router.post("/detect", response_model=DetectResponse)
async def detect_phishing(req: DetectRequest):
    result = analyze_content(req.content)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    log = {
        "content": req.content,
        "verdict": result["verdict"],
        "reasoning": result["reasoning"],
        "suggestion": result["suggestion"],
        "timestamp": datetime.utcnow(),
        "user_feedback": None
    }

    await detections.insert_one(log)
    return result