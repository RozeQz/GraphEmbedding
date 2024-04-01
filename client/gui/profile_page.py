from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget)

from gui.ui_profile import Ui_ProfilePage

from utils.gui import highlight_label


class ProfilePage(QWidget):
    def __init__(self, parent=None):
        super(ProfilePage, self).__init__(parent)
        self.ui = Ui_ProfilePage()
        self.ui.setupUi(self)

        self.parent = parent

        layout = QVBoxLayout(self)
        button = QPushButton('Profile', self)
        layout.addWidget(button)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_profile)
