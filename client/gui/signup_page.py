import os

from PyQt5.QtWidgets import (
    QWidget,
    QLineEdit)

from gui.ui_signup_page import Ui_SignUpPage
from utils.gui import highlight_label
from utils.validator import validate_email, validate_password
from src.api.users_controller import create_user, create_user_data, get_user_data_by_email, get_user_by_login
from src.api.groups_controller import get_group_by_name, create_group, create_user_group

from src.education.user import User


class SignUpPage(QWidget):
    def __init__(self, parent=None):
        super(SignUpPage, self).__init__(parent)
        self.ui = Ui_SignUpPage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        self.path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(self.path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.btn_signup.setStyleSheet(style)

        with open(self.path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.label.setStyleSheet(style)
            self.ui.label_2.setStyleSheet(style)
            self.ui.label_3.setStyleSheet(style)
            self.ui.label_4.setStyleSheet(style)
            self.ui.label_5.setStyleSheet(style)
            self.ui.label_6.setStyleSheet(style)
            self.ui.label_7.setStyleSheet(style)
            self.ui.lbl_fixed_group.setStyleSheet(style)

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
            self.ui.edt_surname.setStyleSheet(style)
            self.ui.edt_name.setStyleSheet(style)
            self.ui.edt_midname.setStyleSheet(style)
            self.ui.edt_email.setStyleSheet(style)
            self.ui.edt_login.setStyleSheet(style)
            self.ui.edt_password.setStyleSheet(style)
            self.ui.edt_group.setStyleSheet(style)

        with open(self.path + "styles/combobox/cbx-main.qss", 'r',
                  encoding="utf-8") as file:
            style = file.read()
            self.ui.cbx_role.setStyleSheet(style)

        # Скрываем пароль
        self.ui.edt_password.setEchoMode(QLineEdit.Password)

        self.ui.edt_password.setToolTip('Пароль должен содержать минимум 8 ' +
                                        'символов, при этом должна ' +
                                        'использоваться хотя бы 1 цифра и ' +
                                        'хотя бы 1 латинская буква.')
        self.ui.lbl_status.hide()

        # Обработка событий
        self.ui.btn_signup.clicked.connect(self.signup)
        self.ui.edt_email.editingFinished.connect(self.check_email)
        self.ui.edt_password.editingFinished.connect(self.check_password)
        self.ui.edt_group.editingFinished.connect(self.check_group)
        self.ui.edt_name.editingFinished.connect(self.check_name)
        self.ui.edt_surname.editingFinished.connect(self.check_surname)
        self.ui.edt_login.editingFinished.connect(self.check_login)
        self.ui.cbx_role.currentIndexChanged.connect(self.change_form)

    def check_login(self) -> bool:
        if self.ui.edt_login.text() != '':
            logins = get_user_by_login(self.ui.edt_login.text())

            if logins is not None:
                with open(self.path + "styles/edit/edt-red.qss", 'r',
                          encoding="utf-8") as file:
                    style = file.read()
                    self.ui.edt_login.setStyleSheet(style)
                self.ui.lbl_status.setText("Пользователь с таким логином" +
                                            " уже существует")
                self.ui.lbl_status.show()
                return False
            else:
                with open(self.path + "styles/edit/edt-green.qss", 'r',
                          encoding="utf-8") as file:
                    style = file.read()
                    self.ui.edt_login.setStyleSheet(style)
                self.ui.lbl_status.hide()
        else:
            with open(self.path + "styles/edit/edt-red.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_login.setStyleSheet(style)
            self.ui.lbl_status.setText("Логин является обязательным полем")
            self.ui.lbl_status.show()
            return False
        return True

    def check_email(self) -> bool:
        try:
            validate_email(self.ui.edt_email.text())
            with open(self.path + "styles/edit/edt-green.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_email.setStyleSheet(style)
            self.ui.lbl_status.hide()
        except ValueError as e:
            with open(self.path + "styles/edit/edt-red.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_email.setStyleSheet(style)
            self.ui.lbl_status.setText(str(e))
            self.ui.lbl_status.show()
            return False

        emails = get_user_data_by_email(self.ui.edt_email.text())
        if emails is not None:
            self.ui.lbl_status.setText("Пользователь с таким email уже " +
                                       "существует")
            self.ui.lbl_status.show()
            return False
        return True

    def check_password(self) -> bool:
        try:
            validate_password(self.ui.edt_password.text())
            with open(self.path + "styles/edit/edt-green.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_password.setStyleSheet(style)
            self.ui.lbl_status.hide()
        except ValueError as e:
            with open(self.path + "styles/edit/edt-red.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_password.setStyleSheet(style)
            self.ui.lbl_status.setText(str(e))
            self.ui.lbl_status.show()
            return False
        return True

    def check_name(self) -> bool:
        if self.ui.edt_name.text() != '':
            with open(self.path + "styles/edit/edt-green.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_name.setStyleSheet(style)
            self.ui.lbl_status.hide()
        else:
            with open(self.path + "styles/edit/edt-red.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_name.setStyleSheet(style)
            self.ui.lbl_status.setText("Имя является обязательным полем")
            self.ui.lbl_status.show()
            return False
        return True

    def check_surname(self) -> bool:
        if self.ui.edt_surname.text() != '':
            with open(self.path + "styles/edit/edt-green.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_surname.setStyleSheet(style)
            self.ui.lbl_status.hide()
        else:
            with open(self.path + "styles/edit/edt-red.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_surname.setStyleSheet(style)
            self.ui.lbl_status.setText("Фамилия является обязательным полем")
            self.ui.lbl_status.show()
            return False
        return True

    def check_group(self) -> bool:
        if self.ui.edt_group.text() != '':
            with open(self.path + "styles/edit/edt-green.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_group.setStyleSheet(style)
            self.ui.lbl_status.hide()
        else:
            with open(self.path + "styles/edit/edt-red.qss", 'r',
                      encoding="utf-8") as file:
                style = file.read()
                self.ui.edt_group.setStyleSheet(style)
            self.ui.lbl_status.setText("Группа является обязательным полем")
            self.ui.lbl_status.show()
            return False
        return True

    def change_form(self):
        if self.ui.cbx_role.currentText() == "Студент":
            self.ui.lbl_fixed_group.setText("Группа:")
            self.ui.edt_group.setPlaceholderText("ИУ6-71Б")
        else:
            self.ui.lbl_fixed_group.setText("Группы:")
            self.ui.edt_group.setPlaceholderText("ИУ6-71Б, ИУ6-72Б (указывайте через запятую)")

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_logo)

    def signup(self):
        if not self.check_email() or not self.check_password() or\
           not self.check_login() or not self.check_group() or\
           not self.check_name() or not self.check_surname():
            return

        user_data = {
            "firstname": self.ui.edt_name.text(),
            "lastname": self.ui.edt_surname.text(),
            "midname": self.ui.edt_midname.text(),
            "email": self.ui.edt_email.text()
        }
        user_data_id = create_user_data(user_data)["id"]

        if self.ui.cbx_role.currentText() == "Студент":
            role = "student"
        else:
            role = "teacher"

        user = {
            "login": self.ui.edt_login.text(),
            "password": self.ui.edt_password.text(),
            "role": role,
            "user_data_id": user_data_id
        }
        user_id = create_user(user)["id"]

        group_names = [group.strip().upper() for group in self.ui.edt_group.text().split(",")]
        for group_name in group_names:
            group = get_group_by_name(group_name)
            if group is None:
                group_id = create_group({"name": group_name})["id"]
            else:
                group_id = group["id"]

            users_group = {
                "user_id": user_id,
                "group_id": group_id
            }
            create_user_group(users_group)

        current_user = User(user_id, role,
                            user_data["firstname"],
                            user_data["lastname"],
                            user_data["midname"])
        self.parent.init_current_user(current_user)

        if role == "student":
            self.parent.ui.stackedWidget.setCurrentWidget(self.parent.student_profile_page)
        else:
            self.parent.ui.stackedWidget.setCurrentWidget(self.parent.teacher_profile_page)
