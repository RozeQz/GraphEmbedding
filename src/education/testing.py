from typing import List
import threading
import sys
from termcolor import colored   # Убрать потом

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
        timer (threading.Timer): Таймер для остановки тестирования.
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
        self.timer = threading.Timer(time, self.stop)
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

    def start(self) -> None:
        '''
        Запуск тестирования.
        '''
        self.timer.start()
        print('Тестирование началось')

        for task in self:
            print(task.question)
            for answer in task.options:
                print(answer, end='\t')
            print()
            answer = input()
            if task.check_answer(answer):
                print(colored('Верно!', 'green'))
                self.points += 1
            else:
                print(colored('Неверно!', 'red'))
            print()
        if self.get_state():
            self.stop(timeout=False)

    def stop(self, timeout: bool = True) -> None:
        '''
        Остановка тестирования.

        Args:
            timeout (bool): Вышло ли время тестирования.
        '''
        try:
            if not timeout:
                self.timer.cancel()
                message = "Вы выполнили все задания. Тестирование завершено!"
            else:
                message = "Время вышло! Тестирование завершено!"
            raise StopTestingException(message)
        except StopTestingException as e:
            self.__stop_handler(e)

    def __stop_handler(self, exception):
        print(exception.message)
        print(f'Ваш результат: {self.points}/{len(self.tasks)}')

    def get_state(self) -> bool:
        '''
        Возвращает статус тестирования.

        Returns:
            bool: True если тестирование еще не завершено, иначе False.
        '''
        return self.timer.is_alive()
