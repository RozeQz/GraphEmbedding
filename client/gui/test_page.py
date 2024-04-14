from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QButtonGroup,
    QLabel,
    QFormLayout,
    QMessageBox)

from gui.ui_test_page import Ui_TestPage

from src.education.task_manager import TaskManager
from utils.gui import (
    clearLayout,
    init_type_1,
    init_type_2,
    init_type_3,
    init_type_4,
    check_answer,
    highlight_label,
    hide_layout_items,
    show_layout_items)

from src.api.results_controller import create_result
from src.api.tests_controller import create_test, create_test_task
from src.education.testing import Testing


MAX_COLUMNS = 3


class CurrentTest():
    test: Testing = None
    test_id: int
    answers: list = []
    current_task: int
    remaining_time: int
    num_tasks: int


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

        self.current_test = CurrentTest()

        # Инициализация всего нужного
        self.options_layout = QVBoxLayout()
        self.group_options = QButtonGroup()
        self.order = None

        self.ui.btn_answer.clicked.connect(self.go_to_next_task)
        self.ui.btn_end.clicked.connect(self.forced_stop)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        # Если тест еще не начат или уже закончен, то запускаем тестирование
        if (self.current_test.test is None) or (not self.timer.isActive()):
            self.start_test()

        highlight_label(self.parent, self.parent.ui.lbl_testing)

    def init_test(self, test_name=None):
        self.current_test.test = self.tm.create_classic_tests()

        if test_name is not None:
            test_id = create_test({"name": test_name})["id"]
        else:
            test_id = create_test({})["id"]

        for task in self.current_test.test.tasks:
            test_task = {
                "test_id": test_id,
                "task_id": task.number
            }
            create_test_task(test_task)

        self.current_test.test_id = test_id
        self.current_test.current_task = 0
        self.current_test.remaining_time = self.current_test.test.time
        self.current_test.num_tasks = len(self.current_test.test.tasks)

    def start_test(self):
        self.tm = TaskManager()

        self.init_test()

        self.timer.start(1000)  # каждую секунду
        self.updateTime()

        # Выводим содержимое главных лейаутов
        show_layout_items(self.ui.hbox_top)
        show_layout_items(self.ui.hbox_main)
        show_layout_items(self.ui.hbox_btn_answer)
        # Убираем результаты
        hide_layout_items(self.ui.vbox_results)

        # Показать сетку заданий
        self.show_grid_tasks()

        # Изначально мы на первом вопросе
        for i in range(self.current_test.num_tasks):
            self.highlight_grid(i, 'grey')

        # Показать первое задание
        self.show_task(self.current_test.current_task)

    def stop_test(self):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()

        # Убираем содержимое главных лейаутов
        hide_layout_items(self.ui.hbox_top)
        hide_layout_items(self.ui.hbox_main)
        hide_layout_items(self.ui.hbox_btn_answer)
        # Выводим результаты
        show_layout_items(self.ui.vbox_results)

        # Отправляем результат на сервер
        result = {
            "user_id": 1,
            "test_id": self.current_test.test_id,
            "points": self.current_test.test.points,
            "time_spent": self.current_test.test.time - self.current_test.remaining_time,
            "answers": self.current_test.answers
        }

        create_result(result)

        self.show_results()

    def show_task(self, task_num: int):
        clearLayout(self.options_layout)

        # Выделяем задание в сетке заданий
        self.highlight_grid(task_num, 'blue')

        task = self.current_test.test.tasks[task_num]

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

    def show_grid_tasks(self):
        square_size = self.ui.gridLayout.geometry().width() // MAX_COLUMNS

        for i in range(self.current_test.num_tasks):
            row = i // MAX_COLUMNS
            column = i % MAX_COLUMNS

            task_number = i + 1
            label = QLabel(str(task_number))
            label.setFixedSize(square_size, square_size)

            with open("client/gui/resources/styles/grid/grid-grey.qss", 'r', encoding="utf-8") as file:
                label.setStyleSheet(file.read())

            self.ui.gridLayout.addWidget(label, row, column)

    def highlight_grid(self, task_number, color: str = 'blue'):
        row = task_number // MAX_COLUMNS
        column = task_number % MAX_COLUMNS

        layout_item = self.ui.gridLayout.itemAtPosition(row, column)
        if layout_item:
            widget = layout_item.widget()  # Приводим к QWidget, если это возможно
            if widget:
                if color == 'blue':
                    with open("client/gui/resources/styles/grid/grid-blue.qss", 'r', encoding="utf-8") as file:
                        widget.setStyleSheet(file.read())
                elif color == 'green':
                    with open("client/gui/resources/styles/grid/grid-green.qss", 'r', encoding="utf-8") as file:
                        widget.setStyleSheet(file.read())
                else:
                    with open("client/gui/resources/styles/grid/grid-grey.qss", 'r', encoding="utf-8") as file:
                        widget.setStyleSheet(file.read())

    def go_to_next_task(self):
        try:
            if check_answer(self, self.current_test.test.tasks[self.current_test.current_task])[0]:
                self.current_test.test.points += 1

            answer = {
                "task_id": self.current_test.test.tasks[self.current_test.current_task].number,
                "answer": check_answer(self, self.current_test.test.tasks[self.current_test.current_task])[1],
                "correct": check_answer(self, self.current_test.test.tasks[self.current_test.current_task])[0]
            }

            self.current_test.answers.append(answer)

            # Выделяем прошлое задание в сетке заданий
            self.highlight_grid(self.current_test.current_task, 'green')

            self.current_test.current_task += 1
            if self.current_test.current_task < self.current_test.num_tasks:
                self.show_task(self.current_test.current_task)
            else:
                self.stop_test()

        except AttributeError:
            mbx = QMessageBox()
            mbx.setIcon(QMessageBox.Critical)
            mbx.setText("Вы не ответили на вопрос! \n" +
                        "Перед тем как перейти к следующему вопросу, нужно ответить на текущий.")
            mbx.setWindowTitle("Внимание!")
            mbx.setStandardButtons(QMessageBox.Ok)
            mbx.exec_()

    def updateTime(self):
        minutes = self.current_test.remaining_time // 60
        seconds = self.current_test.remaining_time % 60
        self.ui.lbl_time.setText(f"До окончания тестирования: {minutes:02}:{seconds:02}")

        self.current_test.remaining_time -= 1

        if self.current_test.remaining_time < 0:
            self.stop_test()

    def show_results(self):
        self.ui.fbox_results.setWidget(0, QFormLayout.LabelRole,
                                       QLabel("Ваш результат: "))
        self.ui.fbox_results.setWidget(0, QFormLayout.FieldRole,
                                       QLabel(f"{self.current_test.test.points}/{self.current_test.num_tasks}"))

        time = self.current_test.test.time - self.current_test.remaining_time
        minutes = time // 60
        seconds = time % 60

        self.ui.fbox_results.setWidget(1, QFormLayout.LabelRole,
                                       QLabel("Время тестирования: "))
        self.ui.fbox_results.setWidget(1, QFormLayout.FieldRole,
                                       QLabel(f"{minutes:02}:{seconds:02}"))

    def forced_stop(self):
        answer = QMessageBox.question(
            self,
            'Подтверждение',
            'Вы уверены, что хотите завершить тестирование? Вы ответили ещё не на все вопросы.',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.stop_test()
        else:
            pass
