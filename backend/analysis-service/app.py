from fastapi import FastAPI, Header
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
sentiment_analyzer = pipeline("sentiment-analysis")

class AnalysisRequest(BaseModel):
    text: str
    user_id: str

@app.post("/analyze")
async def analyze_text(request: AnalysisRequest, authorization: str = Header(...)):
    # Authentication happens at API Gateway level
    result = sentiment_analyzer(request.text)
    return {
        "sentiment": result[0]["label"],
        "score": result[0]["score"],
        "user_id": request.user_id
    }