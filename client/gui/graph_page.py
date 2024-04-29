from typing import List
import os
import time
import numpy as np
import networkx as nx
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from PyQt5.QtCore import Qt, QThreadPool, pyqtSignal, pyqtSlot, QRunnable, QObject
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QSizePolicy,
    QMessageBox)

from gui.ui_graph_page import Ui_GraphPage
from utils.graph import Graph

from gui.mplcanvas import MplCanvas

from src.algorithms.gamma_algorithm import GammaAlgorithm
from src.algorithms.annealing_algorithm import AnnealingAlgorithm
from utils.gui import highlight_label


class NavigationToolbar(NavigationToolbar2QT):
    '''
    Пользовательский тулбар, унаследованный от NavigationToolbar2QT.

    Отображает только кнопки Home, Back, Forward, Pan, Zoom и Save.
    '''
    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] in ('Home', 'Back', 'Forward', 'Pan', 'Zoom', 'Save')]


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    '''
    finished = pyqtSignal()


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # Retrieve args/kwargs here; and fire processing using them
        try:
            self.fn(*self.args, **self.kwargs)
        finally:
            self.signals.finished.emit()  # Done


class GraphPage(QWidget):
    def __init__(self, parent=None):
        super(GraphPage, self).__init__(parent)
        self.ui = Ui_GraphPage()
        self.ui.setupUi(self)

        self.parent = parent

        self.graph = None

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Отображение картинок
        self.ui.lbl_clock.setPixmap(QPixmap(path + "img/clock.png"))

        # Привязка стилей
        with open(path + "styles/button/button-blue.qss", 'r',
                  encoding="utf-8") as file:
            button_style = file.read()
            self.ui.btn_file.setStyleSheet(button_style)
            self.ui.btn_draw.setStyleSheet(button_style)
            self.ui.btn_embed.setStyleSheet(button_style)

        with open(path + "styles/combobox/cbx-main.qss", 'r',
                  encoding="utf-8") as file:
            combo_style = file.read()
            self.ui.cbx_algorithm.setStyleSheet(combo_style)

        with open(path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_file_name.setStyleSheet(label_style)
            self.ui.lbl_algorithm.setStyleSheet(label_style)
            self.ui.lbl_time.setStyleSheet(label_style)

        # Изначально время и информация скрыты
        self.ui.lbl_clock.setVisible(False)
        self.ui.lbl_time.setVisible(False)
        self.ui.lbl_graph_info.setVisible(False)
        self.ui.lbl_file_name.setVisible(False)

        # Изначально некоторые кнопки недоступны
        self.ui.btn_draw.setEnabled(False)
        self.ui.btn_embed.setEnabled(False)

        # Добавляем место для графа на страницу
        self.graph_layout = QVBoxLayout()
        self.ui.horizontalLayout.insertLayout(0, self.graph_layout)

        # Добавление холста для рисования
        self.canvas = MplCanvas(self)
        self.canvas.axes.axis('off')
        # Добавление тулбара на холст
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setVisible(False)
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # Добавление окна загрузки
        self.loading_message_box = QMessageBox()
        self.loading_message_box.setWindowTitle("Информация")
        self.loading_message_box.setText("Процесс укладки запущен. Пожалуйста, подождите.")
        self.loading_message_box.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Связь кнопок
        self.ui.btn_file.clicked.connect(self.open_file)
        self.ui.btn_draw.clicked.connect(self.draw_graph)
        self.ui.btn_embed.clicked.connect(self.embed_graph)

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_graph_emb)

    def open_file(self):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self,
                                                        "Выбрать файл", "",
                                                        filter="Text Files (*.txt)",
                                                        options=options)
        if self.file_name:
            file_base_name = os.path.basename(self.file_name)
            print("Выбранный файл:", self.file_name)
            self.ui.lbl_file_name.setText(file_base_name)
            self.ui.lbl_file_name.setVisible(True)

            # Добавление информации о графе
            self.add_graph_info()

    def add_graph_info(self):
        self.ui.lbl_graph_info.setVisible(True)

        try:
            self.graph = Graph.get_graph_from_file(filename=self.file_name)

            num_vertices = self.graph.size
            num_edges = self.graph.count_edges()
            if self.graph.is_planar():
                is_planar_str = "<p style='color: green;'>Граф планарный"
                self.ui.btn_embed.setEnabled(True)
            else:
                is_planar_str = "<p style='color: red;'>Граф не планарный"
                self.ui.btn_embed.setEnabled(False)

            text = f"<html><head/><body><p>Количество вершин: {num_vertices}</p>" + \
                f"<p>Количество ребер: {num_edges}</p>" + \
                f"{is_planar_str}</p></body></html>"

            self.ui.lbl_graph_info.setText(text)

            self.ui.btn_draw.setEnabled(True)

        except ValueError:
            self.show_error_message("Некорректный файл")

    def draw_graph(self):
        if self.graph is None:
            self.show_error_message("Не выбран файл с графом")
        else:
            self.canvas.axes.cla()

            G = nx.Graph(np.array(self.graph.matrix))
            pos = nx.spring_layout(G)
            nx.draw(G, pos=pos, ax=self.canvas.axes,
                    with_labels=True, node_color="#0C8CE9")
            self.canvas.draw()
            self.toolbar.setVisible(True)

    def get_embedding(self):
        self.canvas.axes.cla()

        alogithm = self.ui.cbx_algorithm.currentIndex()

        start = time.time()

        # Гамма-алгоритм
        if alogithm == 0:
            gr = GammaAlgorithm(self.graph)
            planar = gr.run()
            gr.visualize(canvas=self.canvas)
            self.canvas.draw()
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

        finish = time.time()
        res = finish - start
        res_msec = res * 1000
        self.ui.lbl_time.setText(f"Время работы: {res_msec:.2f} миллисекунд")
        self.ui.lbl_time.setVisible(True)
        self.ui.lbl_clock.setVisible(True)

    def embed_graph(self):
        # Создаем всплывающее окно
        self.show_loading_message()

        # Передаем функцию для выполнения
        worker = Worker(self.get_embedding)
        worker.signals.finished.connect(self.close_loading_message)

        # Запускаем выполнение в потоке
        self.threadpool.start(worker)

    def show_loading_message(self):
        self.loading_message_box.show()

    def close_loading_message(self):
        if self.loading_message_box is not None:
            self.loading_message_box.close()

    def show_error_message(self, text):
        mbx = QMessageBox()
        mbx.setIcon(QMessageBox.Critical)
        if text == "Не выбран файл с графом":
            mbx.setText("Не выбран файл с графом. \n" +
                        "Выберите файл с графом, нажав на кнопку \"Выбрать файл\".")
        elif text == "Некорректный файл":
            mbx.setText("Выбран некорректный файл. \n" +
                        "Выберите текстовый файл, в котором содержится число вершин и матрица смежности заданного графа.")
        mbx.setWindowTitle("Ошибка!")
        mbx.setStandardButtons(QMessageBox.Ok)
        mbx.exec_()
