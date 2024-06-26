import itertools
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

from gui.ui_teacher_task_page import Ui_TeacherTaskPage

from src.education.task import Task
from src.api.tasks_controller import (
    get_all_tasks,
    get_tasks_by_type,
    create_user_task,
    create_task)
from utils.gui import (
    clearLayout,
    clearLineEdits,
    init_type_1,
    init_type_2,
    init_type_3,
    init_type_4,
    check_answer,
    highlight_label)


class TeacherTaskPage(QWidget):
    def __init__(self, parent=None):
        super(TeacherTaskPage, self).__init__(parent)
        self.ui = Ui_TeacherTaskPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        self.path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(self.path + "styles/label/label-h1.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label_3.setStyleSheet(style)

        with open(self.path + "styles/label/label-h2.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.lbl_fixed.setStyleSheet(style)
            self.ui.lbl_fixed_2.setStyleSheet(style)

        with open(self.path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label_2.setStyleSheet(style)
            self.ui.lbl_type.setStyleSheet(style)

        with open(self.path + "styles/button/button-green.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.btn_add_task.setStyleSheet(style)

        with open(self.path + "styles/combobox/cbx-main.qss", 'r',
                  encoding="utf-8") as file:
            combo_style = file.read()
            self.ui.cbx_sort.setStyleSheet(combo_style)
            self.ui.cbx_task_type.setStyleSheet(combo_style)

        with open(self.path + "styles/edit/answer-edit.qss", 'r',
                  encoding="utf-8") as file:
            edt_style = file.read()
            self.ui.pte_answer.setStyleSheet(edt_style)
            self.ui.pte_options.setStyleSheet(edt_style)
            self.ui.pte_task.setStyleSheet(edt_style)

        # Инициализация заданий
        self.init_tasks()

        self.ui.btn_add_task.clicked.connect(self.create_task)
        self.ui.cbx_sort.currentIndexChanged.connect(self.init_tasks)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_tasks)

    def create_task(self):
        question = self.ui.pte_task.text()
        answer = self.ui.pte_answer.text()
        task_type = self.ui.cbx_task_type.currentIndex() + 1
        options = self.ui.pte_options.text()

        task = {
            "question": question,
            "answer": answer,
            "type": task_type,
            "options": options
            }

        create_task(task)
        clearLineEdits(self)

    def init_tasks_layout(self):
        '''
        Инициализация макета для списка заданий.

        Нужно, чтобы при применении фильтров, список можно
        было очистить и перерисовать заново.
        '''
        self.tasks_layout = QVBoxLayout()

        # Обертка для списка заданий
        self.tasks_wrapper = QWidget()
        self.tasks_wrapper.setSizePolicy(QSizePolicy.Preferred,
                                         QSizePolicy.Expanding)
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

    def init_tasks(self):
        # Очистка макета списка заданий
        clearLayout(self.ui.vbox_tasks)

        self.init_tasks_layout()

        tasks = self.get_filtered_tasks()
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
            btn_check.setMinimumWidth(150)
            btn_check.setMaximumWidth(150)
            btn_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            with open(self.path + "styles/button/button-small-blue.qss", 'r',
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
            vertical_spacer = QSpacerItem(20, 7, QSizePolicy.Minimum,
                                          QSizePolicy.Fixed)
            task_layout.addItem(vertical_spacer)
            task_layout.addLayout(hbox_btn_and_results)

            # Отступ между заданиями
            vertical_spacer = QSpacerItem(20, 25, QSizePolicy.Minimum,
                                          QSizePolicy.Fixed)
            task_layout.addItem(vertical_spacer)

            # Добавляем все в главный макет со скроллбаром
            self.tasks_layout.addLayout(task_layout)

            vertical_spacer = QSpacerItem(20, 30, QSizePolicy.Minimum,
                                          QSizePolicy.Expanding)
            self.tasks_layout.addItem(vertical_spacer)

    def check_answer(self, answer_widget, task):
        self.show_result(check_answer(answer_widget, task)[0], answer_widget)

        is_correct = check_answer(answer_widget, task)[0]

        # Если задание решено правиильно
        if is_correct:
            # То обновляем базу данных
            json = {
                "user_id": self.parent.current_user.id,
                "task_id": task.number
            }
            create_user_task(json)

        return is_correct

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

    def get_filtered_tasks(self) -> list:
        '''
        Получить список заданий с учётом фильтров.
        '''
        sorted_tasks = []

        sort_type = self.ui.cbx_sort.currentIndex()

        if sort_type == 0:
            sorted_tasks = get_all_tasks()
        elif sort_type == 1:
            sorted_tasks = list(itertools.chain.from_iterable([
                get_tasks_by_type(1),
                get_tasks_by_type(2),
                get_tasks_by_type(3),
                get_tasks_by_type(4)
            ]))

        return sorted_tasks
