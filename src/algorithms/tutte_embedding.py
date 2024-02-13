'''
Реализация вложения Татта
Tutte Embedding
'''
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
from collections.abc import ValuesView

from utils.algorithm import Algorithm
from utils.graph import Graph
from utils.point import Point


class TutteEmbedding(Algorithm):
    '''
    Реализация вложения Татта простого вершинно
    3-связного планарного графа.
    '''
    def __init__(self, graph: Graph, outer_face: list):
        self.graph = graph
        self.outer_face = outer_face

    def run(self, delta: float = 0.05) -> None:
        '''
        Выполняет алгоритм, вычисляет позицию каждой вершины
        и рисует полученную укладку на плоскости.

        Args:
        delta (float): позиция для сдвига для гарантии плоской укладки.
        '''
        positions = dict(zip(self.outer_face,
                             self.embed_external_face()))
        print(positions)
        weights = defaultdict(lambda: 1)
        vals = list(zip(TutteEmbedding.solve_for(0, self.graph, positions, weights),
                        TutteEmbedding.solve_for(1, self.graph, positions, weights)))

        result = dict(zip(self.graph.keys(), vals))

        self.draw_lines(result, self.graph, delta)
        print(result)
        self.annotate(result)

        plt.axis('off')
        plt.show()

    @staticmethod
    def add_line(point1: Point, point2: Point) -> None:
        '''
        Рисует линию между двумя точками point1 и point2.
        '''
        print("Line: " + str(point1) + "  " + str(point2))
        plt.plot((point1.x, point2.x),
                 (point1.y, point2.y),
                 markerfacecolor='#2C7FB8', markeredgewidth=0,
                 color='black', marker='o',
                 linewidth=1, markersize=18)

    def embed_external_face(self) -> ValuesView:
        '''
        Укладывает внешнюю грань на плоскости.
        '''
        g = nx.Graph()
        for i in range(len(self.outer_face)):
            g.add_edge(i, (i+1) % len(self.outer_face))
        layout = nx.spectral_layout(g)

        return layout.values()

    @staticmethod
    def draw_lines(positions, inp, delta: float = 0.05):
        '''
        Рисует ребра между смежными вершинами.
        Если существуют совпадающие ребра, то одна из вершин будет сдвинута на указанную дельту.

        TODO: высчитывать позицию для сдвига чтобы гарантировать плоскую укладку.
        '''
        for key, value in positions.items():
            positions[key] = list(value)
        for vertex, neighbours in inp.items():
            point1 = Point(positions[vertex][0], positions[vertex][1],
                           label=vertex)
            point2 = Point(positions[neighbours[0]][0], positions[neighbours[0]][1],
                           label=neighbours[0])
            for neighbour in neighbours:
                point3 = Point(positions[neighbour][0], positions[neighbour][1],
                               label=neighbour)
                if point2.label != point3.label:
                    if Point.isBetween(point1, point2, point3):
                        print(f"Точка {point3.label} лежит между {point1.label} и {point2.label}")
                        positions[point3.label][0] += delta
                        positions[point3.label][1] += delta
                        point3.x += delta
                        point3.y += delta
                    elif Point.isBetween(point1, point3, point2):
                        print(f"Точка {point2.label} лежит между {point1.label} и {point3.label}")
                        positions[point2.label][0] += delta
                        positions[point2.label][1] += delta
                        point2.x += delta
                        point2.y += delta
                point2 = point3
                print("From {} to {}".format(vertex, neighbour))
                TutteEmbedding.add_line(point1, point2)

    @staticmethod
    def annotate(positions: dict) -> None:
        '''
        Добавляет название вершин в граф.

        Args:
        positions (dict): Словарь, где ключ - название вершины,
        а значение - координата точки на плоскости.
        '''
        for label, point in positions.items():
            plt.gca().annotate(text=label,
                               xy=point,
                               va="center", ha="center",
                               fontsize=12)

    @staticmethod
    def solve_for(dimension: int, inp: dict, given: dict, weights=None):
        '''
        Решает систему линейных уравнений для нахождения позиций вершин
        '''
        if weights is None:
            weights = defaultdict(lambda: 1)
        equations = np.zeros((len(inp), len(inp)))
        results = np.zeros(len(inp))
        index = list(inp.keys())
        for i, (key, value) in enumerate(inp.items()):
            if key in given:
                results[i] = given[key][dimension]
                equations[i][i] = 1
            else:
                sum_neighbours = sum([weights[x] for x in value])
                for neighbour in value:
                    equations[i][index.index(neighbour)] = weights[neighbour]*(1/sum_neighbours)
                    equations[i][i] = -1
        res = solve(equations, results)
        return res
