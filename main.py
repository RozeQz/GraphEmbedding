from typing import List
import argparse
import networkx as nx

from utils.graph import Graph
from src.algorithms.gamma_algorithm import GammaAlgorithm
from src.algorithms.pqtree_algorithm import PQTreeAlgorithm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', type=str, default="gamma",
                        dest='algorithm',
                        help="Name of algoritm to use: gamma, pq, annealing")
    # parser.add_argument(type=str, dest='filename',
    #                     help="File containing graph")
    args = parser.parse_args()

    algoritm: str = args.algorithm
    vertexes: int = 0
    graph: List[List[int]] = []
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
        gr.show_graph()
        # плоская визуализация
        # gr.show_graph(nx.planar_layout)

        if algoritm == "gamma":
            gr = GammaAlgorithm(gr)
            planar = gr.run()
            if planar is not None:
                print("Граф планарный.")
                print(planar)
            else:
                print("Граф не планарный.")
        elif algoritm == "pq":
            gr = PQTreeAlgorithm(gr)
            planar = gr.run()
            print(planar)
        elif algoritm == "annealing":
            pass

    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()
