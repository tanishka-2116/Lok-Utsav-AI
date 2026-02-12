from fastapi import FastAPI
from pydantic import BaseModel
from festival_brain import get_festival_answer

app = FastAPI()

class Question(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Lok Utsav AI is running"}

@app.post("/ask")
def ask_ai(question: Question):
    response = get_festival_answer(question.query)
    return {"response": response}
