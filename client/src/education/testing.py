from typing import List

from src.education.task import Task


class StopTestingException(Exception):
    '''
    Вызывается, когда тестирование завершается.
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'StopTestingException: {self.message}'
        return 'StopTestingException has been raised'


class Testing():
    '''
    Класс для тестирования знаний пользователя.

    Attributes:
        tasks (List[Task]): Список заданий, включенных в тестирование.
        time (float): Время тестирования в секундах.
        points (int): Количество полученных баллов за тестирование.
        current_task_index (int): Используется при итерировании по заданиям.

    Raises:
        StopTestingException: Когда тестирование завершается.
    '''
    def __init__(self, tasks: List[Task], time: float = 3600):
        '''
        Инициализирует объект класса Testing, предназначенный для тестирования
        знаний пользователя.

        Args:
            tasks (List[Task]): Список заданий, включенных в тестирование.
            time (float): Время тестирования в секундах. По умолчанию тестирование длится час.
        '''
        self.tasks = tasks
        self.time = time
        self.points = 0
        self.current_task_index = None

    def __iter__(self):
        self.current_task_index = 0
        return self

    def __next__(self):
        if self.current_task_index < len(self.tasks):
            current_task = self.tasks[self.current_task_index]
            self.current_task_index += 1
            return current_task
        raise StopIteration
