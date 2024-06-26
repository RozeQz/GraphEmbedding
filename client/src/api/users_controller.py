import requests
import json

from src.api.config import origin


def get_all_users():
    url = origin + "/planared/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_by_id(user_id: int):
    url = origin + f"/planared/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_users_by_role(role: str):
    url = origin + f"/planared/users?role={role}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_data_by_id(data_id: int):
    url = origin + f"/planared/users_data/{data_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_by_user_data(user_data_id: int):
    url = origin + f"/planared/users?user_data_id={user_data_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_data_by_email(email: str):
    url = origin + f"/planared/users_data?email={email}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_by_login(login: str):
    url = origin + f"/planared/users?login={login}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_user_data(user: json):
    url = origin + "/planared/users_data"
    response = requests.post(url, json=user)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_user(user: json):
    url = origin + "/planared/users"
    response = requests.post(url, json=user)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None
