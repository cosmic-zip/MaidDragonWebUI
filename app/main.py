from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse 
from fastapi.responses import RedirectResponse

from core.chat import *
from datetime import datetime

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
context = ""


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
    return FileResponse('templates/index.html')

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


        logs = {
            "status": "success",
            "data": [
                chat_us,
                chat_md,
            ]
        }

        log(prompt, logs)
        return logs

    except Exception as err:

        return  {
            "status": "fail",
            "data": str(err)
        }