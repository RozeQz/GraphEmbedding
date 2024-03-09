import jpype
import jpype.imports
from jpype.types import *

class Connector:
    def __init__(self):
        self.connect()

        from java.util import HashMap

        self.HashMap = HashMap

        self.Graph = jpype.JClass("graph.elements.Graph")
        self.Vertex = jpype.JClass("graph.elements.impl.GraphVertex")
        self.Edge = jpype.JClass("graph.elements.impl.GraphEdge")
        self.STNumbering = jpype.JClass("graph.algorithms.numbering.STNumbering")
        self.Embedding = jpype.JClass("graph.algorithms.planarity.Embedding")
        self.PQTree = jpype.JClass("graph.tree.pq.PQTree")
        self.PQTreePlanarity = jpype.JClass("graph.algorithms.planarity.PQTreePlanarity")
        self.PlanarEmbedding = jpype.JClass("graph.algorithms.planarity.PlanarEmbedding")
        self.PlanarFaces = jpype.JClass("graph.algorithms.planarity.PlanarFaces")

        self.TutteEmbedding = jpype.JClass("graph.algorithms.drawing.TutteEmbedding")

    def __del__(self):
        if jpype.isJVMStarted():
            jpype.shutdownJVM()
        print("Shutdown JVM")

    def connect(self):
        try:
            # Launch the JVM
            if jpype.isJVMStarted():
                return
            jpype.startJVM(jpype.getDefaultJVMPath())
            jar_path = "../lib/GraphDrawingMonoproject-0.1.0-SNAPSHOT-jar-with-dependencies.jar"
            jpype.addClassPath(jar_path)

        except Exception as e:
            raise Exception(f"Failed to launch JVM: {str(e)}")

        self.printConnected()

    def printConnected(self):
        info_msg = "Connected to JVM"
        print(info_msg)
        # logger.info(info_msg)
