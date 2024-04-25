from PyQt5.QtWidgets import (
    QWidget)

from gui.ui_profile import Ui_ProfilePage

from src.api.users_controller import get_user_by_id, get_user_data_by_id
from src.education.user import User
from utils.gui import highlight_label


class ProfilePage(QWidget):
    def __init__(self, parent=None):
        super(ProfilePage, self).__init__(parent)
        self.ui = Ui_ProfilePage()
        self.ui.setupUi(self)

        self.parent = parent

        user = get_user_by_id(1)
        user_data = get_user_data_by_id(user["user_data_id"])

        self.current_user = User(user["id"],
                                 user["role"],
                                 user_data["firstname"],
                                 user_data["lastname"],
                                 user_data["midname"])

        # Инициализация страницы соответствующей роли
        if self.current_user.role == "student":
            # parent.show_student_profile_page()
            pass
        else:
            raise Exception("Invalid role id")

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_profile)
