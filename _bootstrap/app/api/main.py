from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

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

@app.get("/")
def docs():
    return {"status": 200, "message": "OK", "data": "Welcome to the API. Documentation is at /docs"}

@app.post("/")
def hello_world():
    return {"status": 200, "message": "OK", "data": "Hello World"}
