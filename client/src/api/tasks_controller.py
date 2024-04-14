import requests
import json

from src.api.config import origin


def get_all_tasks():
    url = origin + "/planared/tasks/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_task_by_id(task_id: int):
    url = origin + f"/planared/tasks/{task_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_tasks_by_type(task_type: int):
    url = origin + f"/planared/tasks?task_type={task_type}"
    response = requests.get(url)
    if response.status_code == 200:
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
