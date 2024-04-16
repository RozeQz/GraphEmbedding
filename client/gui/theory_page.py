import os

from PyQt5.QtWidgets import (
    QWidget,
    QSizePolicy)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from gui.ui_theory_page import Ui_TheoryPage
from utils.gui import highlight_label


class TheoryPage(QWidget):
    def __init__(self, parent=None):
        super(TheoryPage, self).__init__(parent)
        self.ui = Ui_TheoryPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            button_style = file.read()
            self.ui.btn_read.setStyleSheet(button_style)

        with open(path + "styles/label/label-h2.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_topic_1.setStyleSheet(label_style)
            self.ui.lbl_topic_2.setStyleSheet(label_style)

        with open(path + "styles/label/label-h1.qss", 'r',
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

        # Обработка нажатия на кнопок
        self.ui.lbl_topic_1.mouseReleaseEvent = self.show_topic_1
        self.ui.lbl_topic_2.mouseReleaseEvent = self.show_topic_2

    def show_topic_1(self, event):
        event.accept()
        self.web.setHtml(self.theme_1)

    def show_topic_2(self, event):
        event.accept()
        self.web.setHtml(self.theme_2)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_theory)
