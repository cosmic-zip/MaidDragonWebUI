from typing import Union
from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles
from core.chat import *
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/assets", StaticFiles(directory="./assets", html=True), name="assets")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = []


@app.exception_handler(HTTPException)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": [
            request, exc
        ]},
    )

@app.get("/")
def read_root():
    return FileResponse('index.html')

@app.get("/history")
def chat_history():
    return {
        "data": data
    }

@app.post("/chat/")
def chat_api(prompt: str):

    try:
        chat_us = [
            "{}".format(datetime.now()),
            "user",
            prompt
        ]

        response = chat(prompt)

        chat_md = [
                "{}".format(datetime.now()),
                "maid",
                response
            ]

        data.append(chat_us)
        data.append(chat_md)

        return {
            "status": "success",
            "data": [
                chat_us,
                chat_md,
            ]
        }


    except Exception as e:

        return  {
            "status": "success",
            "data": e
        }