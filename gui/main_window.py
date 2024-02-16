from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QMessageBox
import sys

from gui.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lbl_graph_emb.mouseReleaseEvent = self.foo

    def foo(self, event):
        QMessageBox.information(self, "Clicked", "Label clicked")
