import requests
import json

from src.api.config import origin


def get_all_topics():
    url = origin + "/planared/topics/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_topic_by_id(topic_id: int):
    url = origin + f"/planared/topics/{topic_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_user_topics(user_id: int):
    url = origin + f"/planared/users_topics?user_id={user_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def get_topic_users(group_id: int):
    url = origin + f"/planared/users_topics?group_id={group_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_topic(task: json):
    url = origin + "/planared/topics/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None


def create_user_topic(task: json):
    url = origin + "/planared/users_topics/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None
