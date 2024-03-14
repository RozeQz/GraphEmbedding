from PyQt5.QtWidgets import (QPushButton,
                             QVBoxLayout,
                             QWidget)

class TestPage(QWidget):
    def __init__(self, parent=None):
        super(TestPage, self).__init__()
        self.ui = parent.ui

        layout = QVBoxLayout(self)
        button = QPushButton('Test', self)
        layout.addWidget(button)
