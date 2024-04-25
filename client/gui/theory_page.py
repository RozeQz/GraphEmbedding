import os

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import (
    QWidget,
    QSizePolicy)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from gui.ui_theory_page import Ui_TheoryPage
from utils.gui import highlight_label
from src.api.topics_controller import (
    create_user_topic,
    delete_user_topic,
    get_user_topics)


class TheoryPage(QWidget):
    def __init__(self, parent=None):
        super(TheoryPage, self).__init__(parent)
        self.ui = Ui_TheoryPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        self.path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(self.path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            button_style = file.read()
            self.ui.btn_read.setStyleSheet(button_style)

        with open(self.path + "styles/label/label-h2.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_topic_1.setStyleSheet(label_style)
            self.ui.lbl_topic_2.setStyleSheet(label_style)

        with open(self.path + "styles/label/label-h1.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_topics.setStyleSheet(label_style)

        self.web = QWebEngineView()
        # Загрузка HTML-страницы из файла
        with open("client/gui/theme_1.html", 'r', encoding='utf-8') as f:
            self.theme_1 = f.read()
        with open("client/gui/theme_2.html", 'r', encoding='utf-8') as f:
            self.theme_2 = f.read()

        self.web.setHtml(self.theme_1)
        self.web.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.verticalLayout_2.insertWidget(0, self.web)
        self.ui.verticalLayout_2.setStretch(0, 5)
        self.ui.verticalLayout_2.setStretch(2, 1)

        # TODO: сделать конструктор тем (преподаватель сможет добавлять тему,
        # просто нажав на кнопку, а не чререз qt)
        # Таким образом будет легче находить имеющиеся темы

        # Инициализация текущего топика и топиков
        self.current_topic = 1
        self.topics = [self.theme_1, self.theme_2]

        # Инициализация прочитанных топиков
        self.read_topics = self.refresh_topic_status()

        # Обработка нажатия на кнопок
        self.ui.lbl_topic_1.mouseReleaseEvent = lambda event: self.show_topic(event, 1)
        self.ui.lbl_topic_2.mouseReleaseEvent = lambda event: self.show_topic(event, 2)
        self.ui.btn_read.clicked.connect(self.change_topic_status)

    def show_topic(self, event, num_topic: int):
        event.accept()
        self.current_topic = num_topic

        # Получить объект QLabel по его имени в виде строки
        label_name = f"lbl_topic_{num_topic}"
        label_widget = getattr(self.ui, label_name)

        if self.current_topic in self.read_topics:
            # Меняем цвет и содержимое кнопки
            with open(self.path + "styles/button/button-red.qss", 'r',
                      encoding="utf-8") as file:
                button_style = file.read()
                self.ui.btn_read.setStyleSheet(button_style)
            self.ui.btn_read.setText("Убрать из прочитанного")
            # Меняем цвет темы в оглавлении
            with open(self.path + "styles/label/label-green.qss", 'r',
                      encoding="utf-8") as file:
                label_style = file.read()
                label_widget.setStyleSheet(label_style)
        else:
            # Меняем цвет и содержимое кнопки
            with open(self.path + "styles/button/button-blue.qss", 'r',
                      encoding="utf-8") as file:
                button_style = file.read()
                self.ui.btn_read.setStyleSheet(button_style)
            self.ui.btn_read.setText("Отметить как прочитанное")
            # Меняем цвет темы в оглавлении
            with open(self.path + "styles/label/label-h2.qss", 'r',
                      encoding="utf-8") as file:
                label_style = file.read()
                label_widget.setStyleSheet(label_style)

        self.web.setHtml(self.topics[num_topic - 1])

    def refresh_topic_status(self) -> list:
        topics = []
        for row in get_user_topics(1):
            topics.append(row["topic_id"])
        return topics

    def change_topic_status(self):
        read_flag = False
        # Пока текущий пользователь это пользователь с id=1
        for topic in get_user_topics(1):
            if self.current_topic == topic["topic_id"]:
                read_flag = True
                delete_user_topic(int(topic["id"]))
                break
        # Если топик не был прочитан, то читаем его
        if not read_flag:
            json = {
                "user_id": 1,
                "topic_id": self.current_topic
            }
            create_user_topic(json)

        # При изменении статуса топика, меняем весь массив
        self.read_topics = self.refresh_topic_status()
        # Показываем обновленную страницу
        empty_event = QEvent(QEvent.User)
        self.show_topic(empty_event, self.current_topic)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_theory)
