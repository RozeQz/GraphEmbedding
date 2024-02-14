from typing import List
import argparse
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored   # Убрать потом

from utils.graph import Graph
from src.education.task import Task
from src.education.task_manager import TaskManager
from src.algorithms.gamma_algorithm import GammaAlgorithm
from src.algorithms.pqtree_algorithm import PQTreeAlgorithm
from src.algorithms.annealing_algorithm import AnnealingAlgorithm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', type=str,
                        dest='algorithm',
                        help="Name of algoritm to use: gamma, pq, annealing")
    # parser.add_argument(type=str, dest='filename',
    #                     help="File containing graph")
    args = parser.parse_args()

    algoritm: str = args.algorithm
    vertexes: int = 0
    graph: List[List[int]] = []

    if algoritm is None:
        tm = TaskManager()
        tasks = tm.generate_tasks_by_type(num_tasks=5, task_type=1)
        test = tm.create_test(tasks=tasks, time=20)

        test.start()
        for task in test:
            print(task.question)
            for answer in task.options:
                print(answer, end='\t')
            print()
            answer = input()
            if task.check_answer(answer):
                print(colored('Верно!', 'green'))
            else:
                print(colored('Неврно!', 'red'))
        if test.get_state():
            test.stop()
    else:
        try:
            with open("data/input.txt", "r", encoding="utf-8") as file:
                vertexes = int(file.readline())
                for _ in range(vertexes):
                    row = list(map(int, file.readline().split()))
                    graph.append(row)

            gr = Graph(graph)
            print("Исходный граф:")
            print(gr)

            # исходный граф
            pos = gr.show_graph()
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
                #gr.animate(sec=5)

                new_graph = Graph(graph)
                new_graph = nx.Graph(np.array(new_graph.matrix), nodetype=int)

                nx.draw(new_graph, pos=planar, with_labels=True)
                plt.show()

        except FileNotFoundError as e:
            print(e)


if __name__ == '__main__':
    main()
