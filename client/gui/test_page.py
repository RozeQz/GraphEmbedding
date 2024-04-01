from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QButtonGroup)

from gui.ui_test_page import Ui_TestPage

from src.education.task_manager import TaskManager
from utils.gui import clearLayout, init_type_1, init_type_2, init_type_3, init_type_4, check_answer, highlight_label


class TestPage(QWidget):
    def __init__(self, parent=None):
        super(TestPage, self).__init__(parent)
        self.ui = Ui_TestPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        path = "client/gui/resources/"

        # Отображение картинок
        clock = QPixmap(path + "img/clock.png")
        self.ui.lbl_clock.setPixmap(clock)

        # Инициализация тестирования
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)

        # Инициализация всего нужного
        self.options_layout = QVBoxLayout()
        self.group_options = QButtonGroup()
        self.order = None

        self.task_num = 0

        self.ui.btn_answer.clicked.connect(self.go_to_next_task)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        self.start_test()

        highlight_label(self.parent, self.parent.ui.lbl_testing)

    def closeEvent(self, event):
        # Вызывается при закрытии страницы
        self.stop_test()

    def start_test(self):
        self.tm = TaskManager()
        self.test = self.generate_test()
        self.remaining_time = self.test.time

        self.timer.start(1000)  # каждую секунду
        self.updateTime()

        # Показать первое задание
        self.show_task(self.task_num)

    def stop_test(self):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
        self.show_results()

    def generate_test(self):
        return self.tm.create_classic_tests()

    def show_task(self, task_num: int):
        clearLayout(self.options_layout)

        task = self.test.tasks[task_num]

        self.ui.lbl_num_question.setText(f"Вопрос №{task_num + 1}")
        self.ui.lbl_question.setText(task.question)

        if task.task_type == 1:
            init_type_1(self, self.ui.vbox_task, self.ui.lbl_question, task)
        elif task.task_type == 2:
            init_type_2(self, self.ui.vbox_task, self.ui.lbl_question, task)
        elif task.task_type == 3:
            init_type_3(self, self.ui.vbox_task, self.ui.lbl_question, task)
        elif task.task_type == 4:
            init_type_4(self, self.ui.vbox_task, self.ui.lbl_question, task)

    def go_to_next_task(self):
        if check_answer(self, self.test.tasks[self.task_num]):
            self.test.points += 1

        self.task_num += 1
        if self.task_num < len(self.test.tasks):
            self.show_task(self.task_num)
        else:
            self.stop_test()

    def updateTime(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.ui.lbl_time.setText(f"До окончания тестирования: {minutes:02}:{seconds:02}")

        self.remaining_time -= 1

        if self.remaining_time < 0:
            self.stop_test()

    def show_results(self):
        self.ui.lbl_status.setText("Тестирование завершено!")

        self.ui.lbl_num_question.setText(f'Ваш результат: {self.test.points}/{len(self.test.tasks)}')
