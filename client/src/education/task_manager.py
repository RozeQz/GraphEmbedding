from typing import List
import random

from src.education.database import DataBase
from src.education.task import Task
from src.education.testing import Testing

from src.api.tasks_controller import get_tasks_by_type


class TaskManager():

    def __init__(self):
        pass

    def generate_tasks_by_type(self,
                               num_tasks: int,
                               task_type: int) -> List[Task]:
        '''
        Генерирует список заданий заданного типа.

        Args:
            num_tasks (int): Количество заданий.
            task_type (int): Тип заданий.

        Returns:
            List[Task]: Список объектов типа Task.
        '''
        tasks = []

        all_tasks = get_tasks_by_type(task_type)

        for task in all_tasks:
            tasks.append(Task(number=task["id"],
                              question=task["question"],
                              correct_answer=task["answer"],
                              task_type=task["type"],
                              options=task["options"]))

        return random.choices(tasks, k=num_tasks)

    def create_test(self, tasks: List[Task], time: float = 3600) -> Testing:
        '''
        Создает тест из заданных заданий.

        Args:
            tasks (List[Task]): Список заданий, которые будут включены в тест.
            time (float): Время тестирования в секундах. По умолчанию тестирование длится час.

        Returns:
            Testing: Сгенерированный тест.
        '''
        return Testing(tasks, time)

    def create_classic_tests(self, time: float = 3600):
        '''
        Создает классический тест: по 2 задания каждого типа.

        Args:
            time (float): Время тестирования в секундах. По умолчанию тестирование длится час.

        Returns:
            Testing: Сгенерированный тест.
        '''
        tasks = []
        tasks += self.generate_tasks_by_type(num_tasks=2, task_type=1)
        tasks += self.generate_tasks_by_type(num_tasks=2, task_type=2)
        tasks += self.generate_tasks_by_type(num_tasks=2, task_type=3)
        tasks += self.generate_tasks_by_type(num_tasks=2, task_type=4)
        return self.create_test(tasks, time)
