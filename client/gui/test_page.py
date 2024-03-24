from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import (
    QWidget)

from gui.ui_test_page import Ui_TestPage


class TestPage(QWidget):
    def __init__(self, parent=None):
        super(TestPage, self).__init__(parent)
        self.ui = Ui_TestPage()
        self.ui.setupUi(self)

        # Путь к ассетам
        path = "client/gui/resources/"

        # Отображение картинок
        clock = QPixmap(path + "img/clock.png")
        self.ui.lbl_clock.setPixmap(clock)
