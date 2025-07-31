from fastapi import  FastAPI
from typing import List
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

app = FastAPI()

@app.get("/ping")
def text():
    return Response("Pong")

@app.get("/home")
def Welcome(request = Request):
    with open("Welcomehome.html","r",encoding="utf-8") as  file:
        html_content = file.read()
    return Response(content=html_content, status_code=200,media_type="text/html")

class Object_list(BaseModel):
    author:str
    title:str
    content:str

list_List = List[Object_list]

@app.post("/post")
def post(request = Request):
        return {Object_list}

