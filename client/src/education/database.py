import pandas as pd
import numpy as np


class DataBase():
    def __init__(self):
        data = pd.read_excel('db.xlsx')
        self.tasks = pd.DataFrame(data, columns=['Вопрос',
                                                 'Ответ',
                                                 'Тип',
                                                 'Примечание'])
        self.tasks = self.tasks.replace({np.nan: None})

    def get_tasks_by_type(self, task_type: int):
        return self.tasks[self.tasks['Тип'] == task_type]
