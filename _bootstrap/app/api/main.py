from fastapi import Request,FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import lib 
import json

app = FastAPI()
awx = lib.AWX()

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

@app.get("/storage/job/{id}")
def check_job(id):
    job = awx.check_job(id)
    results = job.json()
    if job.status_code == 200:
        code = 202
        status = results['status']
        data = 'Job ID '+str(results['id'])

        if status in  ["failed", "error", "canceled"]:
            data += results['job_explanation']
            code = 400

        if status == "successful":
            code = 200
            data = results['job_explanation']

        return api_return(code, status, data)

    return api_return(job.status_code,"Error",str(results))



@app.post("/storage/file")
def create_volume(volume: lib.Volume):
    job = awx.launch_job(volume.__dict__, 'ontap_create_volume')
    results = job.json()

    if job.status_code == 201:    
        return api_return(job.status_code, 'Provisioning Job Started', results['id'])
    
    return api_return(job.status_code,"Error",str(results))

@app.post("/storage/block")
def create_lun():
    return api_return(404,"Not Found","This API has not been developed yet")

@app.post("/storage/object")
def create_bucket():
    return api_return(404,"Not Found","This API has not been developed yet")

