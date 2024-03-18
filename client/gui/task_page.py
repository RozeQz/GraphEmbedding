from typing import List
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QCheckBox,
    QLineEdit,
    QRadioButton,
    QButtonGroup,
    QLabel)

from gui.ui_task_page import Ui_TaskPage
# from src.education.task_manager import TaskManager
from src.education.task import Task

from src.api.tasks_controller import get_tasks, create_task


class TaskPage(QWidget):
    def __init__(self, parent=None):
        super(TaskPage, self).__init__(parent)
        self.ui = Ui_TaskPage()
        self.ui.setupUi(self)

        # Шаблон для расположения вариантов ответа
        self.options_layout = QVBoxLayout()

        # Инициализация задания
        self.task = None

        self.ui.btn_get_task.clicked.connect(self.get_task)
        self.ui.btn_add_task.clicked.connect(self.create_task)
        self.ui.btn_check.clicked.connect(self.check_answer)

    def get_task(self):
        tasks = get_tasks()
        task = random.choice(tasks)

        self.task = Task(number=task["id"],
                         question=task["question"],
                         correct_answer=task["answer"],
                         task_type=task["type"],
                         options=task["options"])

        clearLayout(self.options_layout)

        self.ui.lbl_task.setText(self.task.question)
        self.ui.lbl_result.setText("")

        if self.task.task_type == 1:
            self.init_type_1(self.task)
        elif self.task.task_type == 2:
            self.init_type_2(self.task)
        elif self.task.task_type == 3:
            self.init_type_3(self.task)
        elif self.task.task_type == 4:
            self.init_type_4(self.task)

    def init_type_1(self, task):
        options = task.options

        # Создаем новый layout
        self.options_layout = QVBoxLayout()

        # Вставляем новый layout в основной layout
        index = self.ui.verticalLayout_2.indexOf(self.ui.lbl_task)
        self.ui.verticalLayout_2.insertLayout(index + 1, self.options_layout)

        self.group_options = QButtonGroup()

        for option in options:
            radiobutton = QRadioButton(option, self)
            self.options_layout.addWidget(radiobutton)
            self.group_options.addButton(radiobutton)

    def init_type_2(self, task):
        options = task.options

        # Создаем новый layout
        self.options_layout = QVBoxLayout()

        # Вставляем новый layout в основной layout
        index = self.ui.verticalLayout_2.indexOf(self.ui.lbl_task)
        self.ui.verticalLayout_2.insertLayout(index + 1, self.options_layout)

        for option in options:
            checkbox = QCheckBox(option, self)
            self.options_layout.addWidget(checkbox)

    def init_type_3(self, task):
        # Создаем новый layout
        self.options_layout = QVBoxLayout()

        # Вставляем новый layout в основной layout
        index = self.ui.verticalLayout_2.indexOf(self.ui.lbl_task)
        self.ui.verticalLayout_2.insertLayout(index + 1, self.options_layout)

        self.edt_answer = QLineEdit()
        self.edt_answer.setPlaceholderText("Ваш ответ:")
        self.options_layout.addWidget(self.edt_answer)

    def init_type_4(self, task):
        options = task.options

        self.order = options

        # Создаем новый layout
        self.options_layout = QVBoxLayout()

        # Вставляем новый layout в основной layout
        index = self.ui.verticalLayout_2.indexOf(self.ui.lbl_task)
        self.ui.verticalLayout_2.insertLayout(index + 1, self.options_layout)

        for option in options:
            option_layout = QHBoxLayout()  # Горизонтальный макет для варианта и кнопок
            label = QLabel(option)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("QLabel { background-color : lightblue; color : black;}")
            option_layout.addWidget(label)

            # Добавление кнопок
            buttons_layout = QVBoxLayout()
            up_button = QPushButton("↑")
            up_button.setFixedWidth(20)
            buttons_layout.addWidget(up_button)
            down_button = QPushButton("↓")
            down_button.setFixedWidth(20)
            buttons_layout.addWidget(down_button)
            option_layout.addLayout(buttons_layout)

            # Конвертация макета в виджет
            option_widget = QWidget()
            option_widget.setLayout(option_layout)

            # Связка нажатий кнопок с перемещением вариантов
            up_button.clicked.connect(lambda _, lbl=option_widget: self.move_word_up(lbl))
            down_button.clicked.connect(lambda _, lbl=option_widget: self.move_word_down(lbl))

            # Отображение результата
            self.options_layout.addWidget(option_widget)

    def move_word_up(self, widget):
        '''
        Перемещение виджета на 1 элемент выше в шаблоне
        '''
        index = self.options_layout.indexOf(widget)

        if index > 0:
            self.options_layout.insertWidget(index - 1, widget)

            # Изменение порядка ответа
            self.order[index], self.order[index - 1] = self.order[index - 1], self.order[index]

    def move_word_down(self, widget):
        '''
        Перемещение виджета на 1 элемент ниже в шаблоне
        '''
        index = self.options_layout.indexOf(widget)

        if index < self.options_layout.count() - 1:
            self.options_layout.insertWidget(index + 1, widget)

            # Изменение порядка ответа
            self.order[index], self.order[index + 1] = self.order[index + 1], self.order[index]

    def create_task(self):
        question = self.ui.edt_task.text()
        answer = self.ui.edt_answer.text()
        task_type = self.ui.cbx_task_type.currentIndex() + 1
        options = self.ui.edt_options.text()

        task = {
            "question": question,
            "answer": answer,
            "type": task_type,
            "options": options
            }

        create_task(task)

        clearLineEdits(self)

    def check_answer(self):
        if self.task.task_type == 1:
            answer = self.group_options.checkedButton()
            result = self.task.check_answer([answer.text()])
            self.show_result(result)

        elif self.task.task_type == 2:
            answers = []
            for checkbox in self.get_selected_options():
                answers.append(checkbox.text())
            result = self.task.check_answer(answers)
            self.show_result(result)

        elif self.task.task_type == 3:
            answer = self.edt_answer.text()
            result = self.task.check_answer([answer])
            self.show_result(result)

        elif self.task.task_type == 4:
            answer = self.order
            result = self.task.check_answer(answer)
            self.show_result(result)

    def show_result(self, result: bool):
        if result:
            self.ui.lbl_result.setText("Правильно!")
            self.ui.lbl_result.setStyleSheet("color: green;")
        else:
            self.ui.lbl_result.setText("Неправильно!")
            self.ui.lbl_result.setStyleSheet("color: red;")

    def get_selected_options(self) -> List[QCheckBox]:
        '''
        Возвращает список выбранных чекбоксов
        '''
        checked_boxes = []
        for i in range(self.options_layout.count()):
            item = self.options_layout.itemAt(i)
            if isinstance(item.widget(), QCheckBox):
                checkbox = item.widget()
                if checkbox.isChecked():
                    checked_boxes.append(checkbox)
        return checked_boxes


def clearLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

def clearLineEdits(ui):
    for child in ui.findChildren(QLineEdit):
        child.clear()
