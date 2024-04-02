from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
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
                                 user_data["firstname"],
                                 user_data["lastname"],
                                 user_data["midname"])

        self.ui.lbl_surname.setText(self.current_user.lastname)
        self.ui.lbl_name.setText(self.current_user.firstname)
        self.ui.lbl_midname.setText(self.current_user.midname)
        self.ui.lbl_group.setText(self.current_user.groups[0].name)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_profile)
