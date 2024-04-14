import numpy as np
import networkx as nx

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGraphicsDropShadowEffect,
    QWidget,
    QSpacerItem,
    QSizePolicy)

from gui.ui_main_page import Ui_MainPage
from utils.graph import Graph

from gui.mplcanvas import MplCanvas


class MainPage(QWidget):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)

        self.resizeEvent = self.on_resize

        layout = QVBoxLayout(self)

        # Кнопка обновления графа
        self.lbl_refresh = QtWidgets.QLabel(self)
        self.lbl_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_refresh.setObjectName("lbl_refresh")

        # Путь к ассетам
        path = "client/gui/resources/"

        # Отображение картинок
        self.lbl_refresh.setPixmap(QPixmap(path + "img/rotate.png"))

        # Кнопка укладки
        self.btn_embed = QPushButton("Уложить")
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        self.btn_embed.setFont(font)
        self.btn_embed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_embed.setCheckable(False)
        self.btn_embed.setFlat(False)

        # Добавление холста для рисования в главное меню
        self.canvas = MplCanvas(self)
        layout.addWidget(self.canvas)
        self.draw_new_graph()

        # Кнопки для графа на главном меню
        h_layout = QHBoxLayout()
        layout.addLayout(h_layout)
        h_layout.addStretch()
        h_layout.addWidget(self.btn_embed)
        h_layout.addWidget(self.lbl_refresh)

        # Отступы для красоты
        h_spacer = QSpacerItem(20, 0, QSizePolicy.Maximum,
                               QSizePolicy.Maximum)
        h_layout.addItem(h_spacer)

        v_spacer = QSpacerItem(40, 40, QSizePolicy.Maximum,
                               QSizePolicy.Maximum)
        layout.addItem(v_spacer)

        # Настройка этих кнопок
        self.lbl_refresh.setScaledContents(True)
        self.lbl_refresh.setMinimumSize(QSize(90, 60))
        self.lbl_refresh.setMaximumSize(QSize(90, 60))
        self.lbl_refresh.mouseReleaseEvent = self.draw_new_graph

        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(1)
        effect.setOffset(3, 3)
        effect.setColor(QColor(10, 110, 233))
        self.btn_embed.setGraphicsEffect(effect)
        self.btn_embed.setMinimumSize(QSize(160, 50))
        self.btn_embed.setMaximumSize(QSize(160, 50))
        self.btn_embed.setCheckable(True)
        self.btn_embed.toggled.connect(self.embed_graph)

    def draw_new_graph(self, event=None):
        if event is not None:
            event.accept()
        self.canvas.axes.cla()
        graph = Graph.generate_random_planar_graph(10, 0.55)
        # graph = Graph.get_graph_from_file()
        G = nx.Graph(np.array(graph.matrix))
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=self.canvas.axes,
                with_labels=True, node_color="#0C8CE9")
        self.canvas.draw()

    def embed_graph(self, checked: bool):
        if checked:
            # Если кнопка нажата, анимируем нажатие
            self.btn_embed.setStyleSheet("QPushButton { background-color: rgb(10, 110, 233); }")
            self.btn_embed.setGraphicsEffect(None)
            self.btn_embed.move(self.btn_embed.x() + 3,
                                self.btn_embed.y() + 3)

            # Дальше код с анимацией укладки графа
        else:
            # Если кнопка отжата, анимируем отжатие
            self.btn_embed.setStyleSheet("QPushButton { background-color: rgb(12, 140, 233); }")
            effect = QGraphicsDropShadowEffect()
            effect.setBlurRadius(1)
            effect.setOffset(3, 3)
            effect.setColor(QColor(10, 110, 233))
            self.btn_embed.setGraphicsEffect(effect)
            self.btn_embed.move(self.btn_embed.x() - 3,
                                self.btn_embed.y() - 3)

            # Дальше код с анимацией возвращения исходного графа

    def on_resize(self, event):
        event.accept()
        # print(self.size())
