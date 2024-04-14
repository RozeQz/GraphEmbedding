from typing import List
import os
import numpy as np
import networkx as nx

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QSizePolicy)

from gui.ui_graph_page import Ui_GraphPage
from utils.graph import Graph

from gui.mplcanvas import MplCanvas

from src.algorithms.gamma_algorithm import GammaAlgorithm
from src.algorithms.annealing_algorithm import AnnealingAlgorithm
from utils.gui import highlight_label


class GraphPage(QWidget):
    def __init__(self, parent=None):
        super(GraphPage, self).__init__(parent)
        self.ui = Ui_GraphPage()
        self.ui.setupUi(self)

        self.parent = parent

        self.graph = None

        # Добавляем место для графа на страницу
        self.graph_layout = QVBoxLayout()
        self.ui.horizontalLayout.insertLayout(0, self.graph_layout)

        # Добавление холста для рисования
        self.canvas = MplCanvas(self)
        self.canvas.axes.axis('off')
        self.graph_layout.addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Связь кнопок
        self.ui.btn_file.clicked.connect(self.open_file)
        self.ui.btn_draw.clicked.connect(self.draw_graph)
        self.ui.btn_embed.clicked.connect(self.embed_graph)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_graph_emb)

    def open_file(self):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "Text Files (*.txt)", options=options)
        if self.file_name:
            file_base_name = os.path.basename(self.file_name)
            print("Выбранный файл:", self.file_name)
            self.ui.lbl_file_name.setText(file_base_name)

            # Добавление информации о графе
            self.add_graph_info()

    def add_graph_info(self):
        self.graph = Graph.get_graph_from_file(filename=self.file_name)

        num_vertices = self.graph.size
        num_edges = self.graph.count_edges()
        is_planar_str = "<p style='color: green;'>Граф планарный" if self.graph.is_planar() else "<p style='color: red;'>Граф не планарный"

        text = f"<html><head/><body><p>Количество вершин: {num_vertices}</p>" + \
               f"<p>Количество ребер: {num_edges}</p>" + \
               f"{is_planar_str}</p></body></html>"

        self.ui.lbl_graph_info.setText(text)

    def draw_graph(self):
        self.canvas.axes.cla()

        G = nx.Graph(np.array(self.graph.matrix))
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=self.canvas.axes,
                with_labels=True, node_color="#0C8CE9")
        self.canvas.draw()

    def embed_graph(self):
        self.canvas.axes.cla()

        alogithm = self.ui.cbx_algorithm.currentIndex()
        # Гамма-алгоритм
        if alogithm == 0:
            gr = GammaAlgorithm(self.graph)
            planar = gr.run()
            if planar is not None:
                print("Граф планарный.")
                print(planar)
                embed = gr.visualize()
                embed.show()
            else:
                print("Граф не планарный.")
        # Метод отжига
        elif alogithm == 1:
            # Инициализация позиций
            G = nx.Graph(np.array(self.graph.matrix), nodetype=int)
            pos = nx.spring_layout(G)

            gr = AnnealingAlgorithm(self.graph, pos)
            planar = gr.run()
            # gr.animate(sec=5)

            nx.draw(G, pos=planar, ax=self.canvas.axes,
                    with_labels=True, node_color="#0C8CE9")

            self.canvas.draw()

        # PQ-деревья
        elif alogithm == 2:
            G = nx.Graph(np.array(self.graph.matrix), nodetype=int)
            pos = nx.planar_layout(G)
            nx.draw(G, pos=pos, ax=self.canvas.axes,
                    with_labels=True, node_color="#0C8CE9")
            self.canvas.draw()
