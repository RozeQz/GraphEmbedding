import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QWidget)
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
        with open(path + "styles/label/label-h2.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_theme_1.setStyleSheet(label_style)
            self.ui.lbl_theme_2.setStyleSheet(label_style)
            self.ui.lbl_theme_3.setStyleSheet(label_style)

        self.web = QWebEngineView()
        # Загрузка HTML-страницы из файла
        with open("client/gui/theme_1.html", 'r', encoding='utf-8') as f:
            html_content = f.read()
            self.web.setHtml(html_content)
        self.ui.gridLayout.addWidget(self.web)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_theory)
