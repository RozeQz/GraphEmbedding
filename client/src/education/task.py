import textdistance


class Task():
    def __init__(self, number, question, correct_answer, task_type,
                 options=None):
        self.number = number
        self.question = question
        self.task_type = task_type
        if isinstance(correct_answer, int):
            self.correct_answer = [correct_answer]
        else:
            self.correct_answer = correct_answer.split(';')
        if options is not None:
            self.options = options.split(';')
        else:
            self.options = []

    def __str__(self):
        text = (
                    f"Номер вопроса: {self.number}\n"
                    f"Вопрос: {self.question}\n"
                    f"Правильный ответ: {self.correct_answer}\n"
                    f"Тип вопроса: {self.task_type}\n"
                    f"Варианты ответа: {self.options}\n"
                 )
        return text

    def check_answer(self, answer) -> bool:
        '''
        Проверяет, правильный ли дан ответ на задание.

        Args:
        answer (List): Полученный ответ.

        Returns:
        bool: True если ответ правильный, иначе False.
        '''
        # В первом типе заданий правильный ответ один
        if self.task_type == 1:
            if self.correct_answer == answer:
                return True
            return False

        # В задании с множественным ответом надо проверять множество ответов
        if self.task_type == 2:
            if set(self.correct_answer) == set(answer):
                return True
            return False

        # В заданиях с вводом ответа проверяется наличие опечаток
        if self.task_type == 3:
            if Task.is_misspell(self.correct_answer[0], answer[0]):
                return True
            return False

        # В задания с установлением правильной последовательности, проверяется
        # правильность принятого массива
        if self.task_type == 4:
            for i, _ in enumerate(self.correct_answer):
                if self.correct_answer[i].lower() != answer[i].lower():
                    return False
            return True

        # if answer.isdigit():
        #     answer = int(answer)

    @staticmethod
    def is_misspell(correct_text, text) -> bool:
        '''
        Высчитывает расстояние Дамерау — Левенштейна, что позволяет найти
        разницу между двумя последовательностями и выявить опечатки в тексте.

        Args:
        correct_text (str): Правильный текст.
        text (str): Текст для проверки.

        Returns:
        bool: True если допущена опечатка, иначе False.
        '''
        dl = textdistance.DamerauLevenshtein()
        result = dl.normalized_distance(correct_text, text)

        if result > 0.20:
            return False
        return True
