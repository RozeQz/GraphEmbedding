import requests
import json

from src.api.config import origin


def get_all_users():
    url = origin + "/planared/users/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None


def get_user_by_id(user_id: int):
    url = origin + f"/planared/users/{user_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_user_data_by_id(data_id: int):
    url = origin + f"/planared/users_data/{data_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_user(task: json):
    url = origin + "/planared/users/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Error")
        return None