from datetime import datetime
from fastapi import  FastAPI
from typing import List
from pydantic import BaseModel
from starlette.responses import JSONResponse, Response, PlainTextResponse

app = FastAPI()

@app.get("/ping")
def text():
    return Response("Pong",status_code=200)

@app.get("/home")
def Welcome():
    with open("Welcomehome.html","r",encoding="utf-8") as  file:
        html_content = file.read()
    return Response(content=html_content, status_code=200,media_type="text/html")

class Object(BaseModel):
    author:str
    title:str
    content:str
    create_time : datetime

list_List = List[Object]

@app.post("/post" , response_model=List[Object])
def post():
        return {Object}

