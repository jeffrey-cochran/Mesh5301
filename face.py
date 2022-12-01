from half_edge import HalfEdge

class Face(object):

    def __init__(self,*,
        half_edge
    ):
        self.half_edge = half_edge
        return

    def half_edges(self):
        """Iterates over the half edges that loop around the face"""
        next_edge:HalfEdge = None
        current_edge:HalfEdge = self.half_edge
        while next_edge != self.half_edge:
            next_edge = current_edge.next
            yield current_edge
            current_edge = next_edge

