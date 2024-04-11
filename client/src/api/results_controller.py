import requests
import json

from src.api.config import origin
from src.api.tests_controller import get_test_tasks


def get_all_results():
    url = origin + "/planared/results/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_results_by_user(user_id: int):
    url = origin + f"/planared/results?user_id={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_results_by_test(test_id: int):
    url = origin + f"/planared/results?test_id={test_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def calc_average_percent(id: int, obj="user") -> float:
    '''
    Считает средний процент правильных ответов пользователя или конкретного теста.

    Args:
        id (int): ID пользователя или ID теста.
        obj (str): Тип объекта. Если "user", то считается средний процент пользователя. Если "test", то считается средний процент теста.
    '''
    percent = 0
    url = origin + f"/planared/results?{obj}_id={id}"
    response = requests.get(url)
    if response.status_code == 200:
        for result in response.json():
            points = result["points"]
            test_id = result["test_id"]
            num_tasks = len(get_test_tasks(test_id))
            percent += points / num_tasks * 100
        return percent / len(response.json())
    else:
        return None


def create_result(task: json):
    url = origin + "/planared/results/"
    response = requests.post(url, json=task)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")
        return None
