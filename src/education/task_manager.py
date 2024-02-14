from typing import List

from src.education.database import DataBase
from src.education.task import Task
from src.education.testing import Testing


class TaskManager():

    def __init__(self):
        self.db = DataBase()

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
        unique_numbers = set()  # Множество для хранения уникальных номеров заданий
        while len(tasks) < num_tasks:
            row = self.db.get_tasks_by_type(task_type).sample()
            number = row.index[0]
            if number in unique_numbers:
                continue  # Пропустить дубликаты
            unique_numbers.add(number)
            question = row['Вопрос'].values[0]
            correct_answer = row['Ответ'].values[0]
            task_type = row['Тип'].values[0]
            options = row['Примечание'].values[0]
            task = Task(number, question, correct_answer, task_type, options)
            tasks.append(task)
        return tasks

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
