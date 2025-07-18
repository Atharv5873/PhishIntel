from pydantic import BaseModel

class DetectRequest(BaseModel):
    content: str

class DetectResponse(BaseModel):
    verdict: str
    reasoning: str
    suggestion: str
