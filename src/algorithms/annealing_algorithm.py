import math
import random
import networkx as nx
import numpy as np

from utils.graph import Graph
from utils.algorithm import Algorithm
from utils.point import Point

# Коэффициенты для расчета температуры в методе отжига
INITIAL_TEMPERATURE = 100
COOLING_RATE = 0.0003


class AnnealingAlgorithm(Algorithm):
    def __init__(self, graph: Graph, pos: dict):
        self.graph = graph
        self.pos = self.calc_pos(pos)

    def __str__(self):
        coordinates = ''
        for key, value in self.pos.items():
            coordinates += f'{key}: ({value.x}, {value.y})\n'
        return coordinates

    def calc_pos(self, pos) -> dict:
        '''
        Преобразует координаты в объекты класса Point.
        '''
        if pos is None:
            pos = nx.spring_layout(nx.Graph(np.array(self.graph.matrix),
                                            nodetype=int))
        print(pos)
        for key, value in pos.items():
            pos[key] = Point(value[1], value[0])

        return pos

    def count_crossings(self) -> int:
        '''
        Функция, которая возвращает количество пересекающихся ребер в графе.
        '''
        crossings = 0
        for i in range(len(self.graph)):
            for j in range(i+1, len(self.graph)):
                if self.graph.matrix[i][j] == 1:  # Проверяем, есть ли ребро между вершинами i и j
                    for k in range(len(self.graph)):
                        for m in range(k+1, len(self.graph)):
                            if (k != i) and (k != j) and (m != i) and (m != j) and (self.graph.matrix[k][m] == 1):
                                if Point.doIntersect(self.pos[i], self.pos[j], self.pos[k], self.pos[m]):
                                    crossings += 1
        # Проходим по всем ребрам дважды => нужно /2
        return crossings // 2

    @staticmethod
    def from_pos_to_layout(positions) -> dict:
        '''
        Форматирование координат в понятный для networkx вид.
        '''
        layout = {}
        for key, value in positions.items():
            layout[int(key)] = (value.x, value.y)
        return layout

    # Функция, которая реализует метод отжига
    def simulated_annealing(self) -> dict:
        '''
        Симуляция метода отжига.
        '''
        temperature = INITIAL_TEMPERATURE
        while temperature > 1:
            if self.count_crossings() == 0:
                return AnnealingAlgorithm.from_pos_to_layout(self.pos)
            i, j = random.sample(range(len(self.graph)), 2)
            temp1 = self.pos[i]
            temp2 = self.pos[j]
            old_crossings = self.count_crossings()
            self.pos[i], self.pos[j] = self.pos[i].change_position(1), self.pos[j].change_position(1)
            new_crossings = self.count_crossings()
            if new_crossings < old_crossings or math.exp((old_crossings-new_crossings)/temperature) > random.random():
                continue
            self.pos[i], self.pos[j] = temp1, temp2
            temperature *= 1 - COOLING_RATE
            print(temperature)
        return AnnealingAlgorithm.from_pos_to_layout(self.pos)

    def run(self):
        return self.simulated_annealing()
