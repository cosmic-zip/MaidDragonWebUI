from typing import Union
from fastapi import FastAPI
from core.chat import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat/{prompt}")
def chat_api(prompt: str):
    return {
        "chat": prompt, 
        "maid": chat(prompt),
    }