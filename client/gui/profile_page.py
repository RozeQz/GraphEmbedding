from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget)

from gui.ui_profile import Ui_ProfilePage


class ProfilePage(QWidget):
    def __init__(self, parent=None):
        super(ProfilePage, self).__init__(parent)
        self.ui = Ui_ProfilePage()
        self.ui.setupUi(self)

        layout = QVBoxLayout(self)
        button = QPushButton('Profile', self)
        layout.addWidget(button)
