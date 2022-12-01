from edge import Edge
from face import Face
from vertex import Vertex
from half_edge import HalfEdge

class Mesh(object):

    def __init__(self):

        self.E0_signed = None
        self.E1_signed = None
        return