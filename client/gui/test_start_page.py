import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (
    QWidget)

from gui.ui_test_start_page import Ui_TestStartPage
from utils.gui import highlight_label


class TestStartPage(QWidget):
    def __init__(self, parent=None):
        super(TestStartPage, self).__init__(parent)
        self.ui = Ui_TestStartPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            button_style = file.read()
            self.ui.btn_start.setStyleSheet(button_style)
        self.ui.btn_start.setCursor(QCursor(Qt.PointingHandCursor))

        self.ui.btn_start.clicked.connect(self.start_test)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_testing)

    def start_test(self):
        self.parent.ui.stackedWidget.setCurrentWidget(self.parent.test_page)
