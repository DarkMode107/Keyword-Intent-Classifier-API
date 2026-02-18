from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class KeywordRequest(BaseModel):
    keyword: str

@app.get("/")
def home():
    return {"message": "Welcome to the Keyword Intent Classifier API!"}

@app.post("/classify_intent")
def classify_intent(request: KeywordRequest):
    keyword = request.keyword.lower()

    if "buy" in keyword or "price" in keyword or "order" in keyword:
        intent = "Transactional"
    elif "best" in keyword or "vs" in keyword or "review" in keyword:
        intent = "Commercial Investigation"
    elif "login" in keyword or "facebook" in keyword or "youtube" in keyword:
        intent = "Navigational"
    else:
        intent = "Informational"

    return {"keyword": request.keyword, "intent": intent}
