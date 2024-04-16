import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (
    QWidget)

from gui.ui_test_end_page import Ui_TestEndPage
from utils.gui import highlight_label


class TestEndPage(QWidget):
    def __init__(self, result, time, parent=None):
        super(TestEndPage, self).__init__(parent)
        self.ui = Ui_TestEndPage()
        self.ui.setupUi(self)

        self.parent = parent

        self.ui.lbl_result.setText(result)
        self.ui.lbl_time.setText(time)

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            button_style = file.read()
            self.ui.btn_restart.setStyleSheet(button_style)

        self.ui.btn_restart.setCursor(QCursor(Qt.PointingHandCursor))

        with open(path + "styles/label/label-h1.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_test_end.setStyleSheet(label_style)

        with open(path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_result.setStyleSheet(label_style)
            self.ui.lbl_time.setStyleSheet(label_style)
            self.ui.lbl_fixed.setStyleSheet(label_style)
            self.ui.lbl_fixed_2.setStyleSheet(label_style)

        self.ui.btn_restart.clicked.connect(self.restart)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_testing)

    def restart(self):
        self.parent.ui.stackedWidget.setCurrentWidget(self.parent.test_start_page)
