from typing import List
import random
import os

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QButtonGroup)

from gui.ui_task_page import Ui_TaskPage

from src.education.task import Task
from src.api.tasks_controller import get_all_tasks, create_task
from utils.gui import (
    clearLayout,
    clearLineEdits,
    init_type_1,
    init_type_2,
    init_type_3,
    init_type_4,
    check_answer,
    highlight_label)


class TaskPage(QWidget):
    def __init__(self, parent=None):
        super(TaskPage, self).__init__(parent)
        self.ui = Ui_TaskPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(path + "styles/edit/answer-edit.qss", 'r',
                  encoding="utf-8") as file:
            edt_style = file.read()
            self.ui.edt_answer.setStyleSheet(edt_style)
            self.ui.edt_options.setStyleSheet(edt_style)
            self.ui.edt_task.setStyleSheet(edt_style)

        with open(path + "styles/combobox/cbx-main.qss", 'r',
                  encoding="utf-8") as file:
            combo_style = file.read()
            self.ui.cbx_task_type.setStyleSheet(combo_style)

        # Шаблон для расположения вариантов ответа
        self.options_layout = QVBoxLayout()
        self.group_options = QButtonGroup()
        self.order = None

        # Инициализация задания
        self.task = None

        self.ui.btn_get_task.clicked.connect(self.get_task)
        self.ui.btn_add_task.clicked.connect(self.create_task)
        self.ui.btn_check.clicked.connect(self.check_answer)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_tasks)

    def get_task(self):
        tasks = get_all_tasks()
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
            init_type_1(self, self.ui.verticalLayout_2,
                        self.ui.lbl_task, self.task)
        elif self.task.task_type == 2:
            init_type_2(self, self.ui.verticalLayout_2,
                        self.ui.lbl_task, self.task)
        elif self.task.task_type == 3:
            init_type_3(self, self.ui.verticalLayout_2,
                        self.ui.lbl_task, self.task)
        elif self.task.task_type == 4:
            init_type_4(self, self.ui.verticalLayout_2,
                        self.ui.lbl_task, self.task)

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
        self.show_result(check_answer(self, self.task)[0])
        return check_answer(self, self.task)[0]

    def show_result(self, result: bool):
        if result:
            self.ui.lbl_result.setText("Правильно!")
            self.ui.lbl_result.setStyleSheet("color: green;")
        else:
            self.ui.lbl_result.setText("Неправильно!")
            self.ui.lbl_result.setStyleSheet("color: red;")
