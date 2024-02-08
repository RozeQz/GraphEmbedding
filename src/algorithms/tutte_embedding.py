'''
Реализация вложения Татта
Tutte Embedding

Оригинальный код взят с репозитория (автор: @lukas-manduch):
https://github.com/lukas-manduch/tutte-embedding/
'''
import random

from pprint import pprint
import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, ValuesView

from utils.point import Point


class TutteEmbedding():
    def __init__(self):
        pass

    @staticmethod
    def add_line(point1, point2):
        '''
        Рисует линию между двумя точками point1 и point2.
        '''
        x, y = zip(point1, point2)
        print("Line: " + str(x) + "  " + str(y))
        plt.plot(x, y, markerfacecolor='#2C7FB8', markeredgewidth=0,
                 color='black', marker='o',
                 linewidth=1, markersize=18)

    @staticmethod
    def embed_external_face(external_face: list) -> ValuesView:
        '''
        Укладывает внешнюю грань на плоскости.
        '''
        g = nx.Graph()
        for i in range(len(external_face)):
            g.add_edge(i, (i+1) % len(external_face))
        layout = nx.spectral_layout(g)

        return layout.values()

    @staticmethod
    def draw_lines(positions, inp):
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
                        positions[point3.label][0] += 0.05
                        positions[point3.label][1] += 0.05
                    elif Point.isBetween(point1, point3, point2):
                        print(f"Точка {point2.label} лежит между {point1.label} и {point3.label}")
                        positions[point3.label][0] += 0.05
                        positions[point3.label][1] += 0.05
                point2 = point3
                print("From {} to {}".format(vertex, neighbour))
                TutteEmbedding.add_line([positions[vertex][0], positions[vertex][1]],
                        [positions[neighbour][0], positions[neighbour][1]])

    @staticmethod
    def annotate(positions: dict) -> None:
        '''
        Добавляет название вершин в граф
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

    @staticmethod
    def tutte(inp: dict, external_face: list) -> dict:
        '''
        Вложение Татта (Tutte Embedding)
        '''
        positions = dict(zip(external_face,
                             TutteEmbedding.embed_external_face(external_face)))
        pprint(positions)
        weights = defaultdict(lambda: 1)
        vals = list(zip(TutteEmbedding.solve_for(0, inp, positions, weights),
                        TutteEmbedding.solve_for(1, inp, positions, weights)))
        return dict(zip(inp.keys(), vals))
