
from fastapi import FastAPI, Request
from pydantic import BaseModel
from redox import remove_redundant_sentences

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/process/")
def process_text(request: TextRequest):
    optimized = remove_redundant_sentences(request.text)
    return {
        "original_length": len(request.text),
        "optimized_length": len(optimized),
        "optimized_text": optimized,
        "powered_by": "Saber Samir - ReDoX"
    }
