from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edge import Edge
    from vertex import Vertex
    from face import Face

class HalfEdge(object):

    def __init__(self,
        twin:'HalfEdge'=None,
        next:'HalfEdge'=None,
        vertex:'Vertex'=None,
        edge:'Edge'=None,
        face:'Face'=None
    ):

        self.twin = twin
        self.next = next
        self.vertex = vertex
        self.edge = edge
        self.face = face

        return
