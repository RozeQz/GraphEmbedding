from typing import List

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


def clearLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()


def clearLineEdits(ui):
    for child in ui.findChildren(QLineEdit):
        child.clear()


def init_type_1(widget, question_layout, prev_widget, task):
    options = task.options

    # Создаем новый layout
    widget.options_layout = QVBoxLayout()

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    widget.group_options = QButtonGroup()

    for option in options:
        radiobutton = QRadioButton(option, widget)
        widget.options_layout.addWidget(radiobutton)
        widget.group_options.addButton(radiobutton)


def init_type_2(widget, question_layout, prev_widget, task):
    options = task.options

    # Создаем новый layout
    widget.options_layout = QVBoxLayout()

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    for option in options:
        checkbox = QCheckBox(option, widget)
        widget.options_layout.addWidget(checkbox)


def init_type_3(widget, question_layout, prev_widget, task):
    # Создаем новый layout
    widget.options_layout = QVBoxLayout()

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

    widget.edt_answer = QLineEdit()
    widget.edt_answer.setPlaceholderText("Ваш ответ:")
    widget.options_layout.addWidget(widget.edt_answer)


def init_type_4(widget, question_layout, prev_widget, task):
    options = task.options

    widget.order = options

    # Создаем новый layout
    widget.options_layout = QVBoxLayout()

    # Вставляем новый layout в основной layout
    index = question_layout.indexOf(prev_widget)
    question_layout.insertLayout(index + 1, widget.options_layout)

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
        up_button.clicked.connect(lambda _, lbl=option_widget: move_word_up(widget, lbl))
        down_button.clicked.connect(lambda _, lbl=option_widget: move_word_down(widget, lbl))

        # Отображение результата
        widget.options_layout.addWidget(option_widget)


def move_word_up(widget, child_widget):
    '''
    Перемещение виджета на 1 элемент выше в шаблоне
    '''
    index = widget.options_layout.indexOf(child_widget)

    print(widget.order)

    if index > 0:
        widget.options_layout.insertWidget(index - 1, child_widget)

        # Изменение порядка ответа
        widget.order[index], widget.order[index - 1] = widget.order[index - 1], widget.order[index]


def move_word_down(widget, child_widget):
    '''
    Перемещение виджета на 1 элемент ниже в шаблоне
    '''
    index = widget.options_layout.indexOf(child_widget)

    print(widget.order)

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

def check_answer(widget, task) -> bool:
    if task.task_type == 1:
        answer = widget.group_options.checkedButton()
        result = task.check_answer([answer.text()])

    elif task.task_type == 2:
        answers = []
        for checkbox in get_selected_options(widget.options_layout):
            answers.append(checkbox.text())
        result = task.check_answer(answers)

    elif task.task_type == 3:
        answer = widget.edt_answer.text()
        result = task.check_answer([answer])

    elif task.task_type == 4:
        answer = widget.order
        result = task.check_answer(answer)

    return result
