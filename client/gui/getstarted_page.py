import os

from PyQt5.QtWidgets import (
    QWidget)

from gui.ui_getstarted_page import Ui_GetStartedPage
from utils.gui import highlight_label


class GetStartedPage(QWidget):
    def __init__(self, parent=None):
        super(GetStartedPage, self).__init__(parent)
        self.ui = Ui_GetStartedPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.btn_login.setStyleSheet(style)

        with open(path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.lbl_intro.setStyleSheet(style)
            self.ui.lbl_no_acc.setStyleSheet(style)

        with open(path + "styles/label/label-main-blue.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.lbl_signup.setStyleSheet(style)

        self.ui.btn_login.clicked.connect(self.login)
        self.ui.lbl_signup.mouseReleaseEvent = self.signup

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_logo)

    def login(self):
        self.parent.ui.stackedWidget.setCurrentWidget(self.parent.login_page)

    def signup(self, event):
        self.parent.ui.stackedWidget.setCurrentWidget(self.parent.signup_page)
