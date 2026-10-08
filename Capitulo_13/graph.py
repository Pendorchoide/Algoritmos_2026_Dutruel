from typing import Any
from list_ import List

class Graph(List):

    class _nodeVertex:
        def __init__(self, value, other_values = None):
            self.value = value
            self.other_values = other_values
            self.edges = []

        def __str__(self):
            return self.value

    class _nodeEdge():
        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

        def __str__(self):
            return f"{self.weight} - {self.destination}"

    def add_vertex(self, value: Any, other_values = None):
        node_vertex = self._nodeVertex(value, other_values)
        self.append(node_vertex)

    

    def add_edge(self, weight, origin: Any, destination: Any):
        
        pos_origin = self.search(origin)
        if pos_origin is not None:
            print('existe')
        else:
            print('no existe el destino')
            return


g = Graph()

g.add_vertex(7)


g.show()