import jpype
import jpype.imports
from jpype.types import *

from utils.graph import Graph
from utils.algorithm import Algorithm
from utils.connector import Connector

java = Connector()

class PQTreeAlgorithm(Algorithm):

    def __init__(self, graph: Graph):
        self.graph = graph

        jgraph = self.form_java_graph()

        print(jgraph)

        print(f"is biconnected = {jgraph.isBiconnected()}")

        st = jgraph.getEdges().get(0)
        s = st.getOrigin()
        t = st.getDestination()

        print(f"\n{s.getContent()=}\n{t.getContent()=}")


        st_numbering = java.STNumbering(jgraph, s, t)
        st_order = st_numbering.getOrder()
        st_numbers = st_numbering.getNumbering()
        # print(dir(st))

        print(st_numbers)

        pqtree = java.PlanarEmbedding()
        pqtree.emedGraph(jgraph, s, t)

        # planar_faces = java.PlanarFaces(jgraph, st_numbering)
        # planar_faces.formFaces(s, t)
        # print(planar_faces.getPlanarEmbedding())

    def __del__(self):
        if jpype.isJVMStarted():
            jpype.shutdownJVM()

    def form_java_graph(self):
        graph = self.graph.adjacency_matrix_to_edge_list()

        jverts = jpype.java.util.ArrayList()
        size = jpype.java.awt.Dimension(10, 10)
        for i, (key, value) in enumerate(graph.items()):
            content = jpype.java.lang.Integer(key)
            vertex = java.Vertex(size, content)
            jverts.add(vertex)
            print(f"vertex with content {content}")

        jedges = jpype.java.util.ArrayList()
        for i, (key, value) in enumerate(graph.items()):
            vertex1 = jverts[i]
            for v in value:
                vertex2 = jverts[v]
                jedges.add(java.Edge(vertex1, vertex2))
                print(f"edge between {vertex1.getContent()} and {vertex2.getContent()}")

        return java.Graph(jverts, jedges)

    def run(self):
        return "at least works"
