import random

from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
    QCheckBox,
    QLineEdit,
    QRadioButton,
    QButtonGroup
    )

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

        if self.task.task_type == 1:
            self.init_type_1(self.task)

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
            if self.task.check_answer(answer.text()):
                self.ui.lbl_result.setText("Правильно!")
                self.ui.lbl_result.setStyleSheet("color: green;")
            else:
                self.ui.lbl_result.setText("Неправильно!")
                self.ui.lbl_result.setStyleSheet("color: red;")


def clearLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

def clearLineEdits(ui):
    for child in ui.findChildren(QLineEdit):
        child.clear()
