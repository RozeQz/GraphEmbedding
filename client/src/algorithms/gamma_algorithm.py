import copy
import math

from typing import List
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import networkx as nx

from utils.graph import Graph
from utils.algorithm import Algorithm
from src.algorithms.tutte_embedding import TutteEmbedding


class GammaAlgorithm(Algorithm):
    def __init__(self, graph: Graph):
        self.graph = graph

    # DFS алгоритм для нахождения простого цикла
    def dfs_cycle(self, result: list[int], used: list[int], parent: int, v: int) -> bool:
        used[v] = 1

        for i in range(self.graph.size):
            if i == parent:
                continue
            if self.graph.matrix[v][i] == 0:
                continue
            if used[i] == 0:
                result.append(v)
                if self.dfs_cycle(result, used, v, i):
                    # Цикл найден
                    return True
                else:
                    result.pop()
            if used[i] == 1:
                result.append(v)
                # Цикл найден
                cycle = []
                # "Выдергиваем" вершины цикла из порядка обхода
                for idx, vertex in enumerate(result):
                    if vertex == i:
                        cycle.extend(result[idx:])
                        result.clear()
                        result.extend(cycle)
                        return True
                return True
        used[v] = 2
        return False

    def get_cycle(self):
        cycle = []
        has_cycle = self.dfs_cycle(cycle, [0] * self.graph.size, -1, 0)
        if not has_cycle:
            return None
        else:
            return cycle[:]

    # Поиск связных компонент графа G - G', дополненного ребрами из G,
    # один из концов которых принадлежит связной компоненте, а другой G'
    def dfs_segments(self, used: list[int], laid_vertexes: list[bool], result, v: int):
        used[v] = 1
        for i in range(self.graph.size):
            if self.graph.matrix[v][i] == 1:
                result.add_edge(v, i)
                if used[i] == 0 and not laid_vertexes[i]:
                    self.dfs_segments(used, laid_vertexes, result, i)

    def get_segments(self, laid_vertexes: list[bool], edges):
        segments = []
        # Поиск однореберных сегментов
        for i in range(self.graph.size):
            for j in range(i + 1, self.graph.size):
                if self.graph.matrix[i][j] == 1 and not edges[i][j] and laid_vertexes[i] and laid_vertexes[j]:
                    t = Graph(self.graph.size)
                    t.add_edge(i, j)
                    segments.append(t)
        # Поиск связных компонент графа G - G', дополненного ребрами из G,
        # один из концов которых принадлежит связной компоненте, а другой G'
        used = [0] * self.graph.size
        for i in range(self.graph.size):
            if used[i] == 0 and not laid_vertexes[i]:
                res = Graph(self.graph.size)
                self.dfs_segments(used, laid_vertexes, res, i)
                segments.append(res)
        return segments

    # Поиск цепи в выбранном сегменте, используя DFS алгоритм
    def dfs_chain(self, used: list[int], laid_vertexes: list[bool], chain: list[int], v: int):
        used[v] = 1
        chain.append(v)
        for i in range(self.graph.size):
            if self.graph.matrix[v][i] == 1 and used[i] == 0:
                if not laid_vertexes[i]:
                    self.dfs_chain(used, laid_vertexes, chain, i)
                else:
                    chain.append(i)
                return

    def get_chain(self, laid_vertexes: list[bool]) -> list[int]:
        result = []
        for i in range(self.graph.size):
            if laid_vertexes[i]:
                in_graph = False
                for j in range(self.graph.size):
                    if self.graph.contains_edge(i, j):
                        in_graph = True
                if in_graph:
                    self.dfs_chain([0] * self.graph.size, laid_vertexes, result, i)
                    break
        return result

    # Укладка цепи, описание матрицы смежности
    @staticmethod
    def lay_chain(result, chain: list[int], cyclic: bool):
        for i in range(len(chain) - 1):
            result[chain[i]][chain[i + 1]] = True
            result[chain[i + 1]][chain[i]] = True
        if cyclic:
            result[chain[0]][chain[-1]] = True
            result[chain[-1]][chain[0]] = True

    # Проверка на то, что данный сегмент содержится в данной грани
    def is_face_contains_segment(self, face: list[int], segment, laid_vertexes: list[bool]):
        for i in range(self.graph.size):
            for j in range(self.graph.size):
                if segment.contains_edge(i, j):
                    if (laid_vertexes[i] and i not in face) or (laid_vertexes[j] and j not in face):
                        return False
        return True

    # Считаем число граней, вмещающих данные сегменты
    def calc_num_of_faces_contained_segments(self, int_faces, ext_face, segments, laid_vertexes, dest_faces):
        count = [0] * len(segments)
        for i in range(len(segments)):
            for face in int_faces:
                if self.is_face_contains_segment(face, segments[i], laid_vertexes):
                    dest_faces[i] = face
                    count[i] += 1
            if self.is_face_contains_segment(ext_face, segments[i], laid_vertexes):
                dest_faces[i] = ext_face
                count[i] += 1
        return count

    # Получить плоскую укладку графа
    # Возвращаются все грани уложенного планарного графа
    # Если это невозможно(граф не планарный), то None
    def run(self):
        # Если граф одновершинный, то возвращаем две грани
        if self.graph.size == 1:
            faces = []
            outer_face = [0]
            faces.append(outer_face)
            faces.append(list(outer_face))
            return Faces(faces, outer_face)

        # Первый шаг алгоритма:
        # Инициализация: выбираем простой цикл в исходном графе

        # Ищем цикл, если его нет, до граф не соответствует условиям алгоритма
        # (Нет циклов => дерево => планарный)
        c = self.get_cycle()
        if not c:
            return None

        # Списки граней
        ext_face = c[:]
        int_faces = []
        int_faces.append(ext_face)

        # Массивы уже уложенных вершин и ребер соответственно
        laid_vertexes = [False] * self.graph.size
        laid_edges = [[False] * self.graph.size for _ in range(self.graph.size)]

        for i in c:
            laid_vertexes[i] = True

        # Укладываем найденный цикл
        self.lay_chain(laid_edges, c, True)

        num_iter = 0

        # Второй шаг алгоритма:
        # выделение множества сегментов, подсчет числа вмещающих граней,
        # выделение цепей из сегментов, укладка цепей, добавление новых граней
        while True:
            segments = self.get_segments(laid_vertexes, laid_edges)
            # print("Количество сегментов:", len(segments))

            # Если нет сегментов, то граф - найденный простой цикл => планарный
            if not segments:
                break

            # Массив граней, в которые будут уложены соответствующие сегменты с минимальным числом calcNumOfFacesContainedSegments()
            dest_faces = [None] * len(segments)
            count = self.calc_num_of_faces_contained_segments(int_faces, ext_face, segments, laid_vertexes, dest_faces)

            # Ищем минимальное число calcNumOfFacesContainedSegments()
            mi = count.index(min(count))

            # Если хотя бы одно ноль, то граф не планарный
            if count[mi] == 0:
                # print(f"Сегмент {mi} не укладывается в грани.")
                return None
            else:
                # Укладка выбранного сегмента

                # Выделяем цепь между двумя контактными вершинами
                chain = GammaAlgorithm(segments[mi]).get_chain(laid_vertexes)   # Добавлено преобразование типа
                # Целевая грань, куда будет уложен выбранный сегмент
                face = dest_faces[mi]

                # Помечаем вершины цепи как уложенные
                for i in chain:
                    laid_vertexes[i] = True

                # Укладываем соответствующие ребра цепи
                self.lay_chain(laid_edges, chain, False)

                # Ищем номера контактных вершин цепи
                contact_first = -1
                contact_second = -1
                for i, vertex in enumerate(face):
                    if vertex == chain[0]:
                        contact_first = i
                    if vertex == chain[-1]:
                        contact_second = i

                assert contact_first != -1 and contact_second != -1

                # Новые грани, порожденные разбиением грани face выбранным сегментом
                face_size = len(face)
                face1 = []
                face2 = []

                # Находим обратную цепь(цепь, пробегаемая в обратном направлении)
                reverse_chain = list(reversed(chain))

                # Если целевая грань не внешняя
                if face != ext_face:
                    # Укладываем прямую цепь в одну из порожденных граней,
                    # а обратную в другую в зависимости от номеров контактных вершин
                    if contact_first < contact_second:
                        # Первая часть разделения
                        face1.extend(chain)
                        i = (contact_second + 1) % face_size
                        while i != contact_first:
                            face1.append(face[i])
                            i = (i + 1) % face_size

                        # Вторая часть разделения
                        face2.extend(reverse_chain)
                        i = (contact_first + 1) % face_size
                        while i != contact_second:
                            face2.append(face[i])
                            i = (i + 1) % face_size
                    else:
                        # Первая часть разделения
                        face1.extend(reverse_chain)
                        i = (contact_first + 1) % face_size
                        while i != contact_second:
                            face1.append(face[i])
                            i = (i + 1) % face_size

                        # Вторая часть разделения
                        face2.extend(chain)
                        i = (contact_second + 1) % face_size
                        while i != contact_first:
                            face2.append(face[i])
                            i = (i + 1) % face_size

                    # Удаляем целевую грань(она разбилась на две новые)
                    # Добавляем порожденные грани в множество внутренних граней
                    int_faces.remove(face)
                    int_faces.append(face1)
                    int_faces.append(face2)

                # Если целевая грань совпала с внешней
                else:
                    # Все то же самое, только одна из порожденных граней - новая внешняя грань
                    new_outer_face = []
                    if contact_first < contact_second:
                        # Первая часть разделения
                        new_outer_face.extend(chain)
                        i = (contact_second + 1) % face_size
                        while i != contact_first:
                            new_outer_face.append(face[i])
                            i = (i + 1) % face_size

                        # Вторая часть разделения
                        face2.extend(chain)
                        i = (contact_second - 1 + face_size) % face_size
                        while i != contact_first:
                            face2.append(face[i])
                            i = (i - 1 + face_size) % face_size
                    else:
                        # Первая часть разделения
                        face2.extend(reverse_chain)
                        i = (contact_first + 1) % face_size
                        while i != contact_second:
                            face2.append(face[i])
                            i = (i + 1) % face_size

                        # Вторая часть разделения
                        new_outer_face.extend(reverse_chain)
                        i = (contact_first - 1 + face_size) % face_size
                        while i != contact_second:
                            new_outer_face.append(face[i])
                            i = (i - 1 + face_size) % face_size

                    # Удаляем старые, добавляем новые
                    int_faces.append(face2)
                    ext_face = new_outer_face

            # print("Количество граней:", len(int_faces) + 1)
            num_iter += 1

        return Faces(int_faces, ext_face)

    def visualize(self) -> Figure:
        '''
        Визуализирует гамма-алгоритм как вложение Татта.

        Если внешний многоугольник фиксирован (внешняя грань),
        а внутренние вершины являются геометрическим центром соседей,
        то это условие определяет их положения однозначно как решение системы
        линейных уравнений. Решение уравнений даёт планарное вложение.

        Следовательно, зная только внешнюю грань, существует единственная
        плоская укладка внутренних граней.
        '''
        external_face = self.run().external

        graph = self.graph.adjacency_matrix_to_edge_list()
        tutte = TutteEmbedding(graph, external_face)
        return tutte.run(delta=0.05)


class Faces:
    '''
    Класс граней графа.
    '''
    def __init__(self, interior: List[int] = None,
                 external: List[int] = None):
        if interior is not None and external is not None:
            self.interior = [list(face) for face in interior]
            self.external = list(external)
            self.size = len(interior) + 1
        else:
            self.size = 0

    def get_interior(self) -> List[List[int]]:
        '''
        Получить список внутренних граней графа.

        Returns:
        List[List[int]]: Список внутренних граней, заданных списком
        вершин этих граней.
        '''
        return self.interior

    def get_external(self) -> List[int]:
        '''
        Получить внешнюю грань графа.

        Returns:
        List[int]: Список вершин внешней грани.
        '''
        return self.external

    def __str__(self):
        result = (
                    f"Количество граней = {self.size}\n"
                    f"Внешняя грань:\n{self.external}\n"
                    f"Внутренние грани:\n"
                 )
        for face in self.interior:
            result += f"{face}\n"
        return result
