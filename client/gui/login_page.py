import os

from PyQt5.QtWidgets import (
    QWidget,
    QLineEdit)

from gui.ui_login_page import Ui_LoginPage
from utils.gui import highlight_label
from src.api.users_controller import (
    get_user_data_by_email,
    get_user_by_login,
    get_user_data_by_id,
    get_user_by_user_data)

from src.education.user import User


class LoginPage(QWidget):
    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        self.path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(self.path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.btn_login.setStyleSheet(style)

        with open(self.path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label.setStyleSheet(style)
            self.ui.label_2.setStyleSheet(style)

        with open(self.path + "styles/label/label-error.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.lbl_status.setStyleSheet(style)

        with open(self.path + "styles/label/label-h1.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label_8.setStyleSheet(style)

        with open(self.path + "styles/edit/answer-edit.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.edt_email_or_login.setStyleSheet(style)
            self.ui.edt_password.setStyleSheet(style)

        # Скрываем пароль
        self.ui.edt_password.setEchoMode(QLineEdit.Password)

        self.ui.lbl_status.hide()

        # Обработка событий
        self.ui.btn_login.clicked.connect(self.login)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_logo)

    def login(self):
        email = get_user_data_by_email(self.ui.edt_email_or_login.text())
        login = get_user_by_login(self.ui.edt_email_or_login.text())
        if (login is None) and (email is None):
            self.ui.lbl_status.setText("Пользователя с такой почтой или" +
                                       " логином не существует")
            self.ui.lbl_status.show()
            return

        if email is not None:
            user = get_user_by_user_data(email["id"])
        elif login is not None:
            user = login

        password = user["password"]

        if password != self.ui.edt_password.text():
            self.ui.lbl_status.setText("Неверный пароль")
            self.ui.lbl_status.show()
            return
        else:
            user_data = get_user_data_by_id(user["user_data_id"])
            current_user = User(user["id"], user["role"],
                                user_data["firstname"],
                                user_data["lastname"],
                                user_data["midname"])
            self.parent.init_current_user(current_user)

            if user["role"] == "student":
                self.parent.ui.stackedWidget.setCurrentWidget(self.parent.student_profile_page)
            else:
                self.parent.ui.stackedWidget.setCurrentWidget(self.parent.teacher_profile_page)
