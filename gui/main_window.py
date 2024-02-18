import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import (QFont, QFontDatabase, QIcon, QPixmap)
from PyQt5.QtWidgets import (QMainWindow, QLabel,
                             QMessageBox, QPushButton)

from gui.ui_main_window import Ui_MainWindow


class MplCanvas(FigureCanvasQTAgg):
    '''
    Класс для построения графиков matplotlib.
    '''
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Путь к ассетам
        path = "./gui/resources/"

        # Привязка стиля (qss)
        with open(path + "styles/main.qss", 'r', encoding="utf-8") as file:
            self.setStyleSheet(file.read())

        # Отображение картинок
        icon = QIcon()
        icon.addPixmap(QPixmap(path + "img/logo_black.svg"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.ui.lbl_logo.setPixmap(QPixmap(path + "img/logo_white.svg"))
        self.ui.lbl_arrow.setPixmap(QPixmap(path + "img/arrow.svg"))

        # Работа со шрифтом
        font_id = QFontDatabase.addApplicationFont(
            path + "fonts/OpenSans-Regular.ttf")
        if font_id < 0:
            print('Font not loaded')
        families = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(families[0])
        self.ui.lbl_profile.setFont(font)
        print(self.ui.lbl_profile.font().family())

        # Обработка нажатия на кнопку "Укладка графа"
        self.ui.lbl_graph_emb.mouseReleaseEvent = self.foo

        # Отрисовка графика
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        layout = QtWidgets.QVBoxLayout(self.ui.fr_main)
        layout.addWidget(sc)

    def foo(self, event):
        event.accept()
        QMessageBox.information(self, "Clicked", "Label clicked")
