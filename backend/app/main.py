from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from text_generate import textModel
import os
# from model import predict, convert
# sentence_model = SentenceTransformer("all-mpnet-base-v2")

app = FastAPI()

# pydantic models
class sentIn(BaseModel):
    question: str

class sentOut(BaseModel):
    text_tokens: dict
    
model_id = os.path.join(os.getcwd(), "model")
text_obj = textModel(model_id)

@app.post("/text/predict", response_model=sentOut, status_code=200)
def get_prediction(payload:sentIn):
    question_txt = payload.question
    text_result = text_obj.generate_text(question_txt)
    response_object = {
    "text_tokens": text_result
    }
    return response_object