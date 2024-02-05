import math
import random
import networkx as nx
import numpy as np

from utils.graph import Graph
from utils.algorithm import Algorithm

# Коэффициенты для расчета температуры в методе отжига
INITIAL_TEMPERATURE = 100
COOLING_RATE = 0.0003


class Point:
    '''
    https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def change_position(value):
        x = random.random() * value
        y = random.random() * value
        return Point(x, y)

    # Given three collinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'
    @staticmethod
    def onSegment(p, q, r):
        if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
            return True
        return False

    @staticmethod
    def orientation(p, q, r):
        # to find the orientation of an ordered triplet (p,q,r)
        # function returns the following values:
        # 0 : Collinear points
        # 1 : Clockwise points
        # 2 : Counterclockwise

        val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
        if val > 0:
            return 1    # Clockwise orientation
        if val < 0:
            return 2    # Counterclockwise orientation
        return 0        # Collinear orientation

    @staticmethod
    def doIntersect(p1, q1, p2, q2):

        # Find the 4 orientations required for
        # the general and special cases
        o1 = Point.orientation(p1, q1, p2)
        o2 = Point.orientation(p1, q1, q2)
        o3 = Point.orientation(p2, q2, p1)
        o4 = Point.orientation(p2, q2, q1)

        # General case
        if ((o1 != o2) and (o3 != o4)):
            return True

        # Special Cases

        # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
        if ((o1 == 0) and Point.onSegment(p1, p2, q1)):
            return True

        # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
        if ((o2 == 0) and Point.onSegment(p1, q2, q1)):
            return True

        # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
        if ((o3 == 0) and Point.onSegment(p2, p1, q2)):
            return True

        # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
        if ((o4 == 0) and Point.onSegment(p2, q1, q2)):
            return True

        # If none of the cases
        return False

    @staticmethod
    def do_line_segments_intersect(p, p2, q, q2):
        def subtract_points(point1, point2):
            return Point(point1.x - point2.x, point1.y - point2.y)

        r = subtract_points(p2, p)
        s = subtract_points(q2, q)

        def cross_product(point1, point2):
            return point1.x * point2.y - point1.y * point2.x

        u_numerator = cross_product(subtract_points(q, p), r)
        denominator = cross_product(r, s)

        if u_numerator == 0 and denominator == 0:
            # They are coLlinear

            def equal_points(point1, point2):
                return point1 == point2

            # Do they touch? (Are any of the points equal?)
            if equal_points(p, q) or equal_points(p, q2) or equal_points(p2, q) or equal_points(p2, q2):
                return False

            def all_equal(*args):
                first_value = args[0]
                for arg in args[1:]:
                    if arg != first_value:
                        return False
                return True

            # Do they overlap? (Are all the point differences in either direction the same sign)
            return not all_equal(
                (q.x - p.x < 0),
                (q.x - p2.x < 0),
                (q2.x - p.x < 0),
                (q2.x - p2.x < 0)
            ) and not all_equal(
                (q.y - p.y < 0),
                (q.y - p2.y < 0),
                (q2.y - p.y < 0),
                (q2.y - p2.y < 0)
            )

        if denominator == 0:
            # lines are paralell
            return False

        u = u_numerator / denominator
        t = cross_product(subtract_points(q, p), s) / denominator

        return (t >= 0) and (t <= 1) and (u >= 0) and (u <= 1)


class AnnealingAlgorithm(Algorithm):
    def __init__(self, graph: Graph, pos: dict):
        self.graph = graph
        self.pos = self.calc_pos(pos)

    def __str__(self):
        coordinates = ''
        for key, value in self.pos.items():
            coordinates += f'{key}: ({value.x}, {value.y})\n'
        return coordinates

    def calc_pos(self, pos):
        if pos is None:
            pos = nx.spring_layout(nx.Graph(np.array(self.graph.matrix),
                                            nodetype=int))
        print(pos)
        for key, value in pos.items():
            pos[key] = Point(value[1], value[0])

        return pos

    def count_crossings(self):
        '''
        Функция, которая возвращает количество пересекающихся ребер в графе
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

    # Функция, которая реализует метод отжига
    def simulated_annealing(self):
        temperature = INITIAL_TEMPERATURE
        while temperature > 1:
            if self.count_crossings() == 0:
                return AnnealingAlgorithm.from_pos_to_layout(self.pos)
            i, j = random.sample(range(len(self.graph)), 2)
            temp1 = self.pos[i]
            temp2 = self.pos[j]
            old_crossings = self.count_crossings()
            self.pos[i], self.pos[j] = Point.change_position(1), Point.change_position(1)
            new_crossings = self.count_crossings()
            if new_crossings < old_crossings or math.exp((old_crossings-new_crossings)/temperature) > random.random():
                continue
            self.pos[i], self.pos[j] = temp1, temp2
            temperature *= 1 - COOLING_RATE
            print(temperature)
        return AnnealingAlgorithm.from_pos_to_layout(self.pos)

    @staticmethod
    def from_pos_to_layout(positions):
        layout = {}
        for key, value in positions.items():
            layout[int(key)] = (value.x, value.y)
        return layout

    def run(self):
        return self.simulated_annealing()
