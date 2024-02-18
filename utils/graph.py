import copy
from typing import (List, Dict, Mapping, Callable)

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

    def adjacency_matrix_to_edge_list(self) -> Dict[int, List[int]]:
        '''
        Преобразует матрицу смежности в список ребер.

        Например: \n
        0 1 1 1 \n
        1 0 1 1 \n
        1 1 0 1 \t -> \t {0: [1,2,3], 1: [0,2,3], 2: [0,1,3], 3: [0,1,2]} \n
        1 1 1 0 \n

        Returns:
            Dict[int, List[int]]: Список ребер.
        '''
        edge_list: Dict[int, List[int]] = {}
        for i, row in enumerate(self.matrix):
            edge_list[i] = [j for j, value in enumerate(row) if value == 1]
        return edge_list

    @staticmethod
    def get_graph_from_file(filename: str = "data/input.txt") -> 'Graph':
        '''
        Преобразует матрицу смежности, записанную в файле в граф.

        Args:
            filename (str): Путь к файлу с матрицей смежности.

        Returns:
            Graph: Полученный граф.

        Raises:
            FileNotFoundError: Если файла по заданному пути не существует.
        '''
        graph: List[List[int]] = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                vertexes = int(file.readline())
                for _ in range(vertexes):
                    row = list(map(int, file.readline().split()))
                    graph.append(row)
            return Graph(graph)
        except FileNotFoundError as e:
            print(e)

    def show_graph(self, layout: Callable =
                   nx.spring_layout) -> Dict[int, List[float]]:
        """
        Визуализировать исходный граф.

        Args:
            layout: Метод расположения вершин графа.

        Returns:
            Dict[int, List[float]]: Ключ - вершина, значение - координаты вершины.
        """
        graph = nx.Graph(np.array(self.matrix), nodetype=int)
        pos = layout(graph)
        nx.draw(graph, pos=pos, with_labels=True, node_color="#0C8CE9")
        plt.show()
        return pos
