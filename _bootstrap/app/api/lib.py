from typing import Union
from urllib.parse import urlparse
from decouple import config
from pydantic import BaseModel
import requests
import logging
import time


API_BASE = config('TOWER_API_BASE')
API_USERNAME = config('TOWER_USERNAME')
API_PASSWORD = config('TOWER_PASSWORD')
API_TOKEN = config('TOWER_TOKEN')
AUTH_HEADERS = {
    "User-agent": "python-awx-client", 
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(API_TOKEN)
}   

class StorageRequest(BaseModel):
    businessUnit: str
    location: str

class Volume(StorageRequest):
    volume: str
    size: str
    unit: str
    protocol: str

class AWX:
    base = API_BASE
    token = API_TOKEN
    username = API_USERNAME
    password = API_PASSWORD
    headers = {
        "User-agent": "python-awx-client", 
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token) 
    }

    def __init__(self):
        parsed_uri = urlparse(API_BASE)
        self.host = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)

    def check_job(self, id):
        job_status = self.base +'jobs/'+id
    
        job_response = requests.get(job_status, headers=self.headers)
        return job_response  

    def launch_job(self, data, template): 
        base = API_BASE+'job_templates'
        params = {"name":template}
        get = requests.get(base, params, headers=AUTH_HEADERS)
        template = get.json()['results'][0]
        launch_url = template['related']['launch']
        params = {
            'limit': 'cluster1',
            'extra_vars': data
        }
        launch = requests.post(self.host+launch_url, json=params, headers=AUTH_HEADERS)
        return launch
    