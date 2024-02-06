import jpype
import jpype.imports
from jpype.types import *

class Connector:
    def __init__(self):
        self.connect()

        self.Graph = jpype.JClass("graph.elements.Graph")
        self.Vertex = jpype.JClass("graph.elements.impl.GraphVertex")
        self.Edge = jpype.JClass("graph.elements.impl.GraphEdge")
        self.STNumbering = jpype.JClass("graph.algorithms.numbering.STNumbering")
        self.PlanarEmbedding = jpype.JClass("graph.algorithms.planarity.PlanarEmbedding")
        self.PlanarFaces = jpype.JClass("graph.algorithms.planarity.PlanarFaces")

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
