from typing import Union
from fastapi import Request,FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from pydantic import BaseModel
import requests

API_BASE = config('TOWER_API_BASE')
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

class StorageRequest(BaseModel):
    businessUnit: str
    location: str

    def trigger_playbook(playbook): 
        headers = {
            "User-agent": "python-awx-client", 
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(API_TOKEN)
        }
        params = {
            "name":playbook
        }
        template = requests.get(API_BASE+'job_templates', 
                                params, headers=headers)
        return str(template.json()['results'][0]['id'])

@app.get("/")
def docs():
    welcome = "Welcome to the API. Documentation is at /docs"
    return api_return(200,"OK",welcome)

class Volume(StorageRequest):
    volume: str
    size: str
    unit: str
    protocol: str

@app.post("/storage/file")
def create_volume(volume: Volume):
    response = str(volume)+"\n\n"
    response += " Job Template ID = "+Volume.trigger_playbook('ontap_create_volume')

    return api_return(202,"In Development",response)

@app.post("/storage/block")
def create_lun():
    return api_return(404,"Not Found","This API has not been developed yet")

@app.post("/storage/object")
def create_bucket():
    return api_return(404,"Not Found","This API has not been developed yet")

