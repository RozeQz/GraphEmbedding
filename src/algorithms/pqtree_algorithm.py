import jpype
import jpype.imports
from jpype.types import *

from utils.graph import Graph
from utils.algorithm import Algorithm

class PQTreeAlgorithm(Algorithm):
    def __init__(self, graph: Graph):
        self.graph = graph

        # Launch the JVM
        jpype.startJVM(jpype.getDefaultJVMPath())
        jar_path = "../../lib/GraphDrawingMonoproject-0.1.0-SNAPSHOT-jar-with-dependencies.jar"
        jpype.addClassPath(jar_path)

        # Graph(java.util.List<V> vertices, java.util.List<E> edges)
        Graph = jpype.JClass("graph.elements.Graph")
        Vertex = jpype.JClass("graph.elements.impl.GraphVertex")
        Edge = jpype.JClass("graph.elements.impl.GraphEdge")

        vertex1 = Vertex()
        vertex2 = Vertex()

        vertexes = [vertex1, vertex2]
        jvert = jpype.java.util.ArrayList()
        for s in vertexes:
            jvert.add(s)

        edge = Edge(vertex1, vertex2)

        edges = [edge]
        jedges = jpype.java.util.ArrayList()
        for s in edges:
            jedges.add(s)

        graph = Graph(jvert, jedges)

        print(graph)
        print(jvert)
        print(jedges)

    def __del__(self):
        jpype.shutdownJVM()

    def run(self):
        return "at least works"
