import copy

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, m, orientation="undirected"):
        if isinstance(m, int):
            self.size = m
            self.matrix = [[0] * m for _ in range(m)]
        else:
            self.matrix = copy.deepcopy(m)
            self.size = len(m)

        self.orientation = orientation

    def __str__(self):
        output = ""
        for i, row in enumerate(self.matrix):
            output += f"Вершина {i}: "
            connected_nodes = [str(idx) for idx, val in enumerate(row) if val]
            if connected_nodes:
                output += ', '.join(connected_nodes) + "\n"
            else:
                output += "-\n"
        return output

    def __len__(self):
        return self.size

    def add_edge(self, k, m) -> None:
        """
        Добавляет ребро между вершинами k и m в графе.

        Args:
        k (int): Вершина, из которой исходит ребро.
        m (int): Вершина, в которую входит ребро.
        """
        if self.orientation == "directed":
            self.matrix[k][m] = 1
        # Если граф неориентированный, то матрица смежности симметрична
        else:
            self.matrix[k][m] = self.matrix[m][k] = 1

    def contains_edge(self, k: int, m: int) -> bool:
        """
        Проверяет, содержится ли ребро между вершинами k и m
        в графе.

        Args:
        k (int): Вершина, из которой исходит ребро.
        m (int): Вершина, в которую входит ребро.

        Returns:
        bool: True если ребро содержится в графе, иначе False.
        """
        return self.matrix[k][m] == 1

    def num_adjacent_nodes(self, v: int) -> int:
        """
        Возвращает количество смежных узлов для данного узла v.

        Args:
        v (int): Узел, для которого подсчитываются смежные узлы.

        Returns:
        int: Количество смежных узлов с данным узлом v.
        """
        return sum(self.matrix[v])

    def show_graph(self, layout=nx.spring_layout) -> None:
        """
        Визуализировать исходный граф.
        """
        graph = nx.Graph(np.array(self.matrix), nodetype=int)
        pos = layout(graph)
        nx.draw(graph, pos=pos, with_labels=True)
        plt.show()
        return pos
