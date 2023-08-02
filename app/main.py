from typing import Union
from fastapi import FastAPI
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles
from core.chat import *

app = FastAPI()
app.mount("/assets", StaticFiles(directory="./assets", html=True), name="assets")

@app.get("/")
def read_root():
    return FileResponse('index.html')


@app.post("/chat/{prompt}")
def chat_api(prompt: str):
    return {
        "chat": prompt, 
        "maid": chat(prompt),
    }