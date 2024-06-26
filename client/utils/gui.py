from typing import List

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QCheckBox,
    QLineEdit,
    QRadioButton,
    QButtonGroup,
    QLabel,
    QSizePolicy)


# Моя палетка
COLORS = ["#0ACF83", "#1ABCFE", "#A259FF",
          "#F24E1E", "#FF7262", "#636EFA",
          "#FFA15A", "#FF6692", "#C491FB"]


def clearLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()


def clearLineEdits(ui):
    for child in ui.findChildren(QLineEdit):
        child.clear()


def hide_layout_items(layout):
    if layout is None:
        return

    for i in range(layout.count()):
        item = layout.itemAt(i)
        widget = item.widget()
        if widget is not None:
            widget.hide()
        else:
            hide_layout_items(item.layout())


def show_layout_items(layout):
    if layout is None:
        return

    for i in range(layout.count()):
        item = layout.itemAt(i)
        widget = item.widget()
        if widget is not None:
            widget.show()
        else:
            show_layout_items(item.layout())


def init_type_1(widget, question_layout, prev_widget, task):
    '''
    Инициализирует поле ответа на задание первого типа.

    Args:
        widget: Виджет, в котором происходит инициализация.
        question_layout: Лейаут с вопросом.
        prev_widget: Виджет, после которого должны идти варианты ответа.
        task: Само задание.
    '''
    options = task.options

    # Создаем новый layout
    widget.options_layout = QVBoxLayout()
    widget.options_layout.setSpacing(6)

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    widget.group_options = QButtonGroup()

    for option in options:
        radiobutton = QRadioButton(option, widget)
        widget.options_layout.addWidget(radiobutton)
        widget.group_options.addButton(radiobutton)

        with open("client/gui/resources/styles/radio/radio-blue.qss", 'r',
                  encoding="utf-8") as file:
            radio_style = file.read()
            radiobutton.setStyleSheet(radio_style)
        radiobutton.setCursor(QCursor(Qt.PointingHandCursor))


def init_type_2(widget, question_layout, prev_widget, task):
    '''
    Инициализирует поле ответа на задание второго типа.

    Args:
        widget: Виджет, в котором происходит инициализация.
        question_layout: Лейаут с вопросом.
        prev_widget: Виджет, после которого должны идти варианты ответа.
        task: Само задание.
    '''
    options = task.options

    # Создаем новый layout
    widget.options_layout = QVBoxLayout()
    widget.options_layout.setSpacing(6)

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    for option in options:
        checkbox = QCheckBox(option, widget)
        widget.options_layout.addWidget(checkbox)

        with open("client/gui/resources/styles/checkbox/checkbox-blue.qss", 'r',
                  encoding="utf-8") as file:
            checkbox_style = file.read()
            checkbox.setStyleSheet(checkbox_style)
        checkbox.setCursor(QCursor(Qt.PointingHandCursor))


def init_type_3(widget, question_layout, prev_widget):
    '''
    Инициализирует поле ответа на задание третьего типа.

    Args:
        widget: Виджет, в котором происходит инициализация.
        question_layout: Лейаут с вопросом.
        prev_widget: Виджет, после которого должны идти варианты ответа.
    '''
    # Создаем новый layout
    widget.options_layout = QVBoxLayout()
    widget.options_layout.setSpacing(6)

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    widget.edt_answer = QLineEdit()
    widget.edt_answer.setMaximumSize(QSize(1000, 50))
    widget.edt_answer.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
    widget.edt_answer.setPlaceholderText("Ваш ответ:")
    widget.options_layout.addWidget(widget.edt_answer)

    with open("client/gui/resources/styles/edit/answer-edit.qss", 'r',
              encoding="utf-8") as file:
        edt_style = file.read()
        widget.edt_answer.setStyleSheet(edt_style)


def init_type_4(widget, question_layout, prev_widget, task):
    '''
    Инициализирует поле ответа на задание четвертого типа.

    Args:
        widget: Виджет, в котором происходит инициализация.
        question_layout: Лейаут с вопросом.
        prev_widget: Виджет, после которого должны идти варианты ответа.
        task: Само задание.
    '''
    options = task.options

    widget.order = options

    # Создаем новый layout
    widget.options_layout = QVBoxLayout()
    widget.options_layout.setSpacing(6)

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    for option in options:
        option_layout = QHBoxLayout()  # Горизонтальный макет для варианта и кнопок
        label = QLabel(option)
        label.setAlignment(Qt.AlignCenter)

        with open("client/gui/resources/styles/label/label-task4.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            label.setStyleSheet(label_style)

        option_layout.addWidget(label)

        # Добавление кнопок
        buttons_layout = QVBoxLayout()
        up_button = QPushButton()
        up_button.setFixedWidth(20)
        up_button.setFlat(True)
        up_button.setCursor(QCursor(Qt.PointingHandCursor))
        buttons_layout.addWidget(up_button)
        down_button = QPushButton()
        down_button.setFixedWidth(20)
        down_button.setFlat(True)
        down_button.setCursor(QCursor(Qt.PointingHandCursor))
        buttons_layout.addWidget(down_button)
        option_layout.addLayout(buttons_layout)

        with open("client/gui/resources/styles/button/button-arrow-up.qss",
                  'r', encoding="utf-8") as file:
            button_style = file.read()
            up_button.setStyleSheet(button_style)

        with open("client/gui/resources/styles/button/button-arrow-down.qss",
                  'r', encoding="utf-8") as file:
            button_style = file.read()
            down_button.setStyleSheet(button_style)

        # Конвертация макета в виджет
        option_widget = QWidget()
        option_widget.setLayout(option_layout)

        # Связка нажатий кнопок с перемещением вариантов
        up_button.clicked.connect(lambda _, lbl=option_widget: move_word_up(widget, lbl))
        down_button.clicked.connect(lambda _, lbl=option_widget: move_word_down(widget, lbl))

        # Отображение результата
        widget.options_layout.addWidget(option_widget)


def move_word_up(widget, child_widget):
    '''
    Перемещение виджета на 1 элемент выше в шаблоне
    '''
    index = widget.options_layout.indexOf(child_widget)

    if index > 0:
        widget.options_layout.insertWidget(index - 1, child_widget)

        # Изменение порядка ответа
        widget.order[index], widget.order[index - 1] = widget.order[index - 1], widget.order[index]


def move_word_down(widget, child_widget):
    '''
    Перемещение виджета на 1 элемент ниже в шаблоне
    '''
    index = widget.options_layout.indexOf(child_widget)

    if index < widget.options_layout.count() - 1:
        widget.options_layout.insertWidget(index + 1, child_widget)

        # Изменение порядка ответа
        widget.order[index], widget.order[index + 1] = widget.order[index + 1], widget.order[index]


def get_selected_options(options_layout) -> List[QCheckBox]:
    '''
    Возвращает список выбранных чекбоксов
    '''
    checked_boxes = []
    for i in range(options_layout.count()):
        item = options_layout.itemAt(i)
        if isinstance(item.widget(), QCheckBox):
            checkbox = item.widget()
            if checkbox.isChecked():
                checked_boxes.append(checkbox)
    return checked_boxes


def check_answer(widget, task) -> tuple:
    '''
    Проверяет ответ на задание.

    Args:
        widget: Виджет с заданием.
        task: Само задание.

    Returns:
        tuple: Результат проверки и ответ на задание
    '''
    if task.task_type == 1:
        try:
            answer = widget.group_options.checkedButton().text()
        except AttributeError:
            raise AttributeError("No answer")
        result = task.check_answer([answer])

    elif task.task_type == 2:
        answer = []
        for checkbox in get_selected_options(widget.options_layout):
            answer.append(checkbox.text())
        if not answer:
            raise AttributeError("No answer")
        result = task.check_answer(answer)

    elif task.task_type == 3:
        answer = widget.edt_answer.text()
        if not answer:
            raise AttributeError("No answer")
        result = task.check_answer([answer])

    elif task.task_type == 4:
        answer = widget.order
        result = task.check_answer(answer)

    return (result, answer)


def highlight_label(widget, label):
    '''
    Делает все лейблы меню белыми, а заданный лейбл меню синим.
    '''
    labels = [widget.ui.lbl_profile,
              widget.ui.lbl_theory,
              widget.ui.lbl_tasks,
              widget.ui.lbl_testing,
              widget.ui.lbl_graph_emb,
              widget.ui.lbl_exit]

    for lbl in labels:
        lbl.setStyleSheet("color: rgb(255, 255, 255)")

    label.setStyleSheet("color: rgb(12, 140, 233)")
