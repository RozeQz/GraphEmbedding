import requests
import json


origin = "http://localhost:8000"

def get_tasks():
    url = origin + "/planared/tasks/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None

def create_task(task: json):
    url = origin + "/planared/tasks/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Error")
        return None
