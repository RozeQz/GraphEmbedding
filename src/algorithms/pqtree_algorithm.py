import jpype

from utils.graph import Graph
from utils.algorithm import Algorithm
from utils.connector import Connector

class PQTreeAlgorithm(Algorithm):
    def __init__(self, graph: Graph):
        self.graph = graph
        self.java = Connector()

    def form_java_graph(self):
        graph = self.graph.adjacency_matrix_to_edge_list()

        jverts = jpype.java.util.ArrayList()
        size = jpype.java.awt.Dimension(10, 10)
        for i, (key, value) in enumerate(graph.items()):
            content = jpype.java.lang.Integer(key)
            vertex = self.java.Vertex(size, content)
            jverts.add(vertex)
            print(f"Vertex {vertex} with content {content}")

        jedges = jpype.java.util.ArrayList()
        for i, (key, value) in enumerate(graph.items()):
            vertex1 = jverts[i]
            for v in value:
                vertex2 = jverts[v]
                edge = self.java.Edge(vertex1, vertex2)
                jedges.add(edge)
                print(f"Edge {edge} between {vertex1.getContent()} and {vertex2.getContent()}")

        return self.java.Graph(jverts, jedges)

    def run(self):
        jgraph = self.form_java_graph()

        print(jgraph)

        print(f"is biconnected = {jgraph.isBiconnected()}")

        st = jgraph.getEdges().get(0)
        s = st.getOrigin()
        t = st.getDestination()

        print(f"{s.getContent()=}\n{t.getContent()=}")

        print('\n ST numbering\n')

        st_numbering = self.java.STNumbering(jgraph, s, t)
        st_order = st_numbering.getOrder()
        st_numbers = st_numbering.getNumbering()
        # print(dir(st))

        print('\n Planar Embedding\n')

        # embedding = self.java.Embedding(self.java.HashMap, st_numbers)

        # Либо ошибка в программе на java, либо ошибка возникает на этапе преобразования типов в jpype
        # Ошибка java.lang.NullPointerException: Cannot invoke "java.util.Collection.toArray()" because "c" is null
        # возникает на этапе проверки графа на планарность .isPlannar(graph) внутри этого метода

        # Более того, после работы алгоритма, библиотека не предусматривает вычисление координат
        # вершин на плоскости. В коде библиотеки очень много вставок "TODO", что говорит
        # о неполноценности библиотеки => принято решение отказаться от данного алгоритма.
        try:
            embedding = self.java.PlanarEmbedding().emedGraph(jgraph, s, t)
            print(f"{embedding.toString()}")
            print('\ngetEmbedding\n')
            print(f"{embedding.getEmbedding()=}")
            for e in embedding.getEmbedding().entrySet():
                print(e)
            print('\ngetStNumbering\n')
            print(f"{embedding.getStNumbering()=}")
            for e in embedding.getStNumbering().entrySet():
                print(e)

        except jpype.JException as ex:
            print(f"Java Exception while running PQTree embedding: {str(ex)}")
