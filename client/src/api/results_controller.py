import requests
import json

from src.api.config import origin


def get_all_results():
    url = origin + "/planared/results/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None


def get_results_by_user(user_id: int):
    url = origin + f"/planared/results?user_id={user_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None


def get_results_by_test(test_id: int):
    url = origin + f"/planared/results?test_id={test_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None


def create_result(task: json):
    url = origin + "/planared/results/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Error")
        return None
