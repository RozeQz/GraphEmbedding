from src.education.database import DataBase
from src.education.task import Task


class TaskManager():

    def __init__(self):
        self.db = DataBase()

    def generate_tasks_by_type(self, num_tasks: int, task_type: int) -> list:
        '''
        Генерирует список заданий заданного типа.

        Args:
        num_tasks (int): Количество заданий.
        task_type (int): Тип заданий.

        Returns:
        list[Task]: Список объектов типа Task.
        '''
        tasks = []
        for _ in range(num_tasks):
            row = self.db.get_tasks_by_type(task_type).sample()
            number = row.index[0]
            question = row['Вопрос'].values[0]
            correct_answer = row['Ответ'].values[0]
            task_type = row['Тип'].values[0]
            options = row['Примечание'].values[0]
            task = Task(number, question, correct_answer, task_type, options)
            tasks.append(task)
        return tasks
