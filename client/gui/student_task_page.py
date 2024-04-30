from typing import List
import os

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QButtonGroup,
    QLabel,
    QPushButton,
    QScrollArea,
    QSpacerItem,
    QSizePolicy)

from gui.ui_student_task_page import Ui_StudentTaskPage

from src.education.task import Task
from src.api.tasks_controller import get_all_tasks
from utils.gui import (
    init_type_1,
    init_type_2,
    init_type_3,
    init_type_4,
    check_answer,
    highlight_label)


class StudentTaskPage(QWidget):
    def __init__(self, parent=None):
        super(StudentTaskPage, self).__init__(parent)
        self.ui = Ui_StudentTaskPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        self.path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(self.path + "styles/label/label-h1.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label_3.setStyleSheet(style)

        with open(self.path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label_2.setStyleSheet(style)

        with open(self.path + "styles/radio/radio-blue.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.rdb_hide_solved.setStyleSheet(style)

        with open(self.path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.btn_search.setStyleSheet(style)

        with open(self.path + "styles/combobox/cbx-main.qss", 'r',
                  encoding="utf-8") as file:
            combo_style = file.read()
            self.ui.cbx_sort.setStyleSheet(combo_style)

        self.tasks_layout = QVBoxLayout()

        # Обертка для списка заданий
        self.tasks_wrapper = QWidget()
        self.tasks_wrapper.setStyleSheet("background-color: #ffffff")
        self.tasks_wrapper.setLayout(self.tasks_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.tasks_wrapper)
        self.ui.vbox_tasks.addWidget(scroll_area)

        with open(self.path + "styles/scrollbar/scrollbar.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            scroll_area.setStyleSheet(style)

        # Инициализация заданий
        self.init_tasks()

        # self.ui.btn_get_task.clicked.connect(self.get_task)
        # self.ui.btn_add_task.clicked.connect(self.create_task)
        # self.ui.btn_check.clicked.connect(self.check_answer)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_tasks)

    def init_tasks(self):
        tasks = get_all_tasks()
        for task in tasks:
            task = Task(number=task["id"],
                        question=task["question"],
                        correct_answer=task["answer"],
                        task_type=task["type"],
                        options=task["options"])

            task_layout = QVBoxLayout()

            lbl_task_title = QLabel(f"{task.number}. {task.question}")

            with open(self.path + "styles/label/label-main.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                lbl_task_title.setStyleSheet(style)

            task_layout.addWidget(lbl_task_title)

            # Шаблон для расположения вариантов ответа
            answer_widget = QWidget()
            answer_widget.options_layout = QVBoxLayout()
            answer_widget.group_options = QButtonGroup()
            answer_widget.order = None

            # Инициализация вариантов ответа по типу задания
            if task.task_type == 1:
                init_type_1(answer_widget, task_layout, lbl_task_title, task)
            elif task.task_type == 2:
                init_type_2(answer_widget, task_layout, lbl_task_title, task)
            elif task.task_type == 3:
                init_type_3(answer_widget, task_layout, lbl_task_title)
            elif task.task_type == 4:
                init_type_4(answer_widget, task_layout, lbl_task_title, task)

            # Добавение кнопки "Ответить"
            btn_check = QPushButton("Ответить")
            btn_check.setMinimumWidth(200)
            btn_check.setMaximumWidth(200)
            btn_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            with open(self.path + "styles/button/button-blue.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                btn_check.setStyleSheet(style)

            # Добавляем результат проверки
            answer_widget.lbl_result = QLabel()
            answer_widget.lbl_result_icon = QLabel()

            # Привязка функции на нажатие кнопки
            btn_check.clicked.connect(lambda _, widget=answer_widget, t=task:
                                      self.check_answer(widget, t))

            # Результат проверки будет находиться справа от кнопки "Ответить"
            hbox_btn_and_results = QHBoxLayout()
            hbox_btn_and_results.setSpacing(10)

            # Слева кнопка, справа - результат
            hbox_btn_and_results.addWidget(btn_check)
            hbox_btn_and_results.addWidget(answer_widget.lbl_result_icon)
            hbox_btn_and_results.addWidget(answer_widget.lbl_result)
            horizontal_spacer = QSpacerItem(100, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Fixed)
            hbox_btn_and_results.addItem(horizontal_spacer)

            # Отступ между ответами и кнопкой
            vertical_spacer = QSpacerItem(20, 13, QSizePolicy.Minimum,
                                          QSizePolicy.Fixed)
            task_layout.addItem(vertical_spacer)
            task_layout.addLayout(hbox_btn_and_results)

            # Отступ между заданиями
            vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                          QSizePolicy.Fixed)
            task_layout.addItem(vertical_spacer)

            # Добавляем все в главный макет со скроллбаром
            self.tasks_layout.addLayout(task_layout)

    def check_answer(self, answer_widget, task):
        self.show_result(check_answer(answer_widget, task)[0], answer_widget)
        return check_answer(answer_widget, task)[0]

    def show_result(self, result: bool, answer_widget):
        if result:
            answer_widget.lbl_result.setText("Правильно")
            with open(self.path + "styles/label/label-correct.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                answer_widget.lbl_result.setStyleSheet(style)
            icon = QPixmap(self.path + "img/icons8-tick.svg")
            answer_widget.lbl_result_icon.setPixmap(icon)
        else:
            answer_widget.lbl_result.setText("Неправильно")
            with open(self.path + "styles/label/label-incorrect.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                answer_widget.lbl_result.setStyleSheet(style)
            icon = QPixmap(self.path + "img/icons8-cross.svg")
            answer_widget.lbl_result_icon.setPixmap(icon)
