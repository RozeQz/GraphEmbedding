import requests
import json

from src.api.config import origin


def get_all_tasks():
    url = origin + "/planared/tasks"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_task_by_id(task_id: int):
    url = origin + f"/planared/tasks/{task_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_tasks_by_type(task_type: int):
    url = origin + f"/planared/tasks?task_type={task_type}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_tasks(user_id: int):
    url = origin + f"/planared/users_tasks?user_id={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_task_users(task_id: int):
    url = origin + f"/planared/users_tasks?task_id={task_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_task(task: json):
    url = origin + "/planared/tasks"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_user_task(user_task: json):
    url = origin + "/planared/users_tasks"
    response = requests.post(url, json=user_task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def delete_user_task(user_task_id: int):
    url = origin + f"/planared/users_tasks/{user_task_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
