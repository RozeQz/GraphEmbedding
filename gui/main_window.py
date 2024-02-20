from typing import List
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import (QFont, QFontDatabase, QIcon, QPixmap, 
                         QCursor, QColor)
from PyQt5.QtWidgets import (QMainWindow, QLabel,
                             QMessageBox, QPushButton,
                             QVBoxLayout, QHBoxLayout,
                             QGraphicsDropShadowEffect)

from gui.ui_main_window import Ui_MainWindow
from utils.graph import Graph


class MplCanvas(FigureCanvasQTAgg):
    '''
    Класс для отображения графиков matplotlib.
    '''
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(1, 1, 1)
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
        self.ui.lbl_refresh.setPixmap(QPixmap(path + "img/rotate.png"))

        # Работа со шрифтом
        font_id = QFontDatabase.addApplicationFont(
            path + "fonts/OpenSans-Regular.ttf")
        if font_id < 0:
            print('Font not loaded')
        families = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(families[0])
        self.ui.lbl_profile.setFont(font)

        # Обработка нажатия на кнопку "Укладка графа"
        self.ui.lbl_graph_emb.mouseReleaseEvent = self.foo

        # Добавление холста для рисования в главное меню
        self.canvas = MplCanvas(self)
        layout = QVBoxLayout(self.ui.fr_main)
        layout.addWidget(self.canvas)
        self.draw_new_graph()

        # Кнопки для графа на главном меню
        h_layout = QHBoxLayout()
        layout.addLayout(h_layout)
        h_layout.addStretch()
        h_layout.addWidget(self.ui.btn_embed)
        h_layout.addWidget(self.ui.lbl_refresh)

        # Настройка этих кнопок
        self.ui.lbl_refresh.setScaledContents(True)
        self.ui.lbl_refresh.setMinimumSize(QSize(90, 60))
        self.ui.lbl_refresh.setMaximumSize(QSize(90, 60))
        self.ui.lbl_refresh.mouseReleaseEvent = self.draw_new_graph

        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(1)
        effect.setOffset(3, 3)
        effect.setColor(QColor(10, 110, 233))
        self.ui.btn_embed.setGraphicsEffect(effect)
        self.ui.btn_embed.setMinimumSize(QSize(160, 50))
        self.ui.btn_embed.setMaximumSize(QSize(160, 50))
        self.ui.btn_embed.setCheckable(True)
        self.ui.btn_embed.toggled.connect(self.embed_graph)

    def draw_new_graph(self, event=None):
        if event is not None:
            event.accept()
        self.canvas.axes.cla()
        graph = Graph.generate_random_planar_graph(15, 0.33)
        # graph = Graph.get_graph_from_file()
        G = nx.Graph(np.array(graph.matrix))
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=self.canvas.axes,
                with_labels=True, node_color="#0C8CE9")
        self.canvas.draw()

    def embed_graph(self, checked: bool):
        if checked:
            # Если кнопка нажата, анимируем нажатие
            self.ui.btn_embed.setStyleSheet("QPushButton { background-color: rgb(10, 110, 233); }")
            self.ui.btn_embed.setGraphicsEffect(None)
            self.ui.btn_embed.move(self.ui.btn_embed.x() + 3,
                                   self.ui.btn_embed.y() + 3)

            # Дальше код с анимацией укладки графа
        else:
            # Если кнопка отжата, анимируем отжатие
            self.ui.btn_embed.setStyleSheet("QPushButton { background-color: rgb(12, 140, 233); }")
            effect = QGraphicsDropShadowEffect()
            effect.setBlurRadius(1)
            effect.setOffset(3, 3)
            effect.setColor(QColor(10, 110, 233))
            self.ui.btn_embed.setGraphicsEffect(effect)
            self.ui.btn_embed.move(self.ui.btn_embed.x() - 3,
                                   self.ui.btn_embed.y() - 3)

            # Дальше код с анимацией возвращения исходного графа

    def foo(self, event):
        event.accept()
        QMessageBox.information(self, "Clicked", "Label clicked")
