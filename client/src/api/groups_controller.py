import requests
import json

from src.api.config import origin


def get_all_groups():
    url = origin + "/planared/groups/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_group_by_id(group_id: int):
    url = origin + f"/planared/groups/{group_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_group_by_name(name: str):
    url = origin + f"/planared/groups?name={name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_groups(user_id: int):
    url = origin + f"/planared/users_groups?user_id={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_group_users(group_id: int):
    url = origin + f"/planared/users_groups?group_id={group_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_group(group: json):
    url = origin + "/planared/groups"
    response = requests.post(url, json=group)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_user_group(user_group: json):
    url = origin + "/planared/users_groups"
    response = requests.post(url, json=user_group)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None
