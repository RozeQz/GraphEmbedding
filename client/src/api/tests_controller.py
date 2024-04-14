import requests
import json

from src.api.config import origin


def get_all_tests():
    url = origin + "/planared/tests/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_test_tasks(test_id: int):
    url = origin + f"/planared/tasks_tests/{test_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_test(task: json):
    url = origin + "/planared/tests/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_test_task(task: json):
    url = origin + "/planared/tasks_tests/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None
