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
        answer (str): Полученный ответ.

        Returns:
        bool: True если ответ правильный, иначе False.
        '''
        # В заданиях с вводом ответа проверяется наличие опечаток
        if self.task_type == 3:
            if Task.is_misspell(self.correct_answer, answer):
                return True
            return False

        # if answer.isdigit():
        #     answer = int(answer)

        # В остальных задания правильный ответ лишь один
        for correct_answer in self.correct_answer:
            if str(answer).lower() == str(correct_answer).lower():
                return True
        return False

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
