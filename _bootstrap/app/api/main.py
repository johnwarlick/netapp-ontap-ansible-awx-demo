from typing import Union
from fastapi import Request,FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from pydantic import BaseModel

API_USERNAME = config('TOWER_USERNAME')
API_PASSWORD = config('TOWER_PASSWORD')
API_TOKEN = config('TOWER_TOKEN')

app = FastAPI()

origins = [
    "http://localhost",
    "http://awx.demo.netapp.com:8080",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def api_return(status,message,data):
    return {"status": status, "message": message, "data": data}

@app.get("/")
def docs():
    welcome = "Welcome to the API. Documentation is at /docs"
    return api_return(200,"OK",welcome)

class Volume(BaseModel):
    volume: str
    size: str
    unit: str
    protocol: str

@app.post("/storage/file")
def create_volume(volume: Volume):
    return api_return(202,"In Development","This API is currently being developed")

@app.post("/storage/block")
def create_lun():
    return api_return(404,"Not Found","This API has not been developed yet")

@app.post("/storage/object")
def create_bucket():
    return api_return(404,"Not Found","This API has not been developed yet")
