from typing import List
import argparse
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored   # Убрать потом
import json

from PyQt5 import QtWidgets, QtGui, uic
import sys

from utils.graph import Graph
from src.education.task import Task
from src.education.task_manager import TaskManager
from src.algorithms.gamma_algorithm import GammaAlgorithm
from src.algorithms.pqtree_algorithm import PQTreeAlgorithm
from src.algorithms.annealing_algorithm import AnnealingAlgorithm
from gui.main_window import MainWindow

from src.models.tasks import crud, schemas
from configs.database import session_factory, engine
from src.models.models import Base

def main() -> None:

    with session_factory() as session:
        Base.metadata.create_all(engine)

        task = schemas.TaskCreate(question='foo', answer='bar', type=1,
                                  options='bar, baz')
        crud.create_tasks(session, task)

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', type=str,
                        dest='algorithm',
                        help="Name of algoritm to use: gamma, pq, annealing")
    parser.add_argument('-g', '--gui', action='store_true')
    # parser.add_argument(type=str, dest='filename',
    #                     help="File containing graph")
    args = parser.parse_args()

    algoritm: str = args.algorithm
    vertexes: int = 0
    graph: List[List[int]] = []

    if args.gui:
        app = QtWidgets.QApplication([])
        application = MainWindow()
        # application = uic.loadUi("gui/ui_main_window.ui")
        application.show()

        sys.exit(app.exec())

    if algoritm is None:
        tm = TaskManager()
        tasks = tm.generate_tasks_by_type(num_tasks=5, task_type=1)
        test = tm.create_test(tasks=tasks, time=20)

        test.start()

    else:
        gr = Graph.get_graph_from_file(filename="data/input.txt")

        print("Исходный граф:")
        print(gr)

        # исходный граф
        pos = gr.show_graph()
        print(pos)
        # плоская визуализация
        # gr.show_graph(nx.planar_layout)

        if algoritm == "gamma":
            gr = GammaAlgorithm(gr)
            planar = gr.run()
            if planar is not None:
                print("Граф планарный.")
                print(planar)
                gr.visualize()
            else:
                print("Граф не планарный.")
        elif algoritm == "pq":
            gr = PQTreeAlgorithm(gr)
            gr.run()
        elif algoritm == "annealing":
            gr = AnnealingAlgorithm(gr, pos)
            planar = gr.run()
            # gr.animate(sec=5)

            new_graph = Graph(graph)
            new_graph = nx.Graph(np.array(new_graph.matrix), nodetype=int)

            nx.draw(new_graph, pos=planar, with_labels=True,
                    node_color="#0C8CE9")
            plt.show()


if __name__ == '__main__':
    main()
