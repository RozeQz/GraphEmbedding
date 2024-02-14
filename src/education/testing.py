from typing import List
import threading

from src.education.task import Task


class Testing():
    def __init__(self, tasks: List[Task], time: float = 3600):
        '''
        Инициализирует объект класса Testing, предназначенный для тестирования
        знаний пользователя.

        Args:
            tasks (List[Task]): Список заданий, включенных в тестирование.
            time (float): Время тестирования в секундах. По умолчанию тестирование длится час.
            current_task_index (int): Используется при итерировании по заданиям.
        '''
        self.tasks = tasks
        self.timer = threading.Timer(time, self.stop)
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

    def stop(self) -> None:
        '''
        Остановка тестирования.
        '''
        self.timer.cancel()
        print('Тестирование завершено')

    def get_state(self) -> bool:
        '''
        Возвращает статус тестирования.

        Returns:
            bool: True если тестирование еще не завершено, иначе False.
        '''
        return self.timer.is_alive()
