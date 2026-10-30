from graph import Graph
from typing import Any
# A)
casa = Graph(False)

casa.add_vertex("cocina")
casa.add_vertex("comedor")
casa.add_vertex("cochera")
casa.add_vertex("quincho")
casa.add_vertex("baño 1")
casa.add_vertex("baño 2")
casa.add_vertex("habitacion 1")
casa.add_vertex("habitacion 2")
casa.add_vertex("sala de estar")
casa.add_vertex("terraza")
casa.add_vertex("patio")

# B)
casa.add_edge(5, "cocina", "baño 1")
casa.add_edge(5, "cocina", "cochera")
casa.add_edge(3, "cocina", "comedor")
casa.add_edge(3, "cocina", "patio")
casa.add_edge(2, "cocina", "quincho")
casa.add_edge(5, "cocina", "baño 2")
casa.add_edge(5, "cocina", "habitacion 1")
casa.add_edge(7, "cocina", "terraza")


casa.add_edge(2, "comedor", "sala de estar")
casa.add_edge(3, "comedor", "baño 1")
casa.add_edge(4, "comedor", "terraza")
casa.add_edge(6, "comedor", "baño 2")
casa.add_edge(3, "comedor", "habitacion 1")


casa.add_edge(5, "cochera", "patio")
casa.add_edge(2, "cochera", "quincho")

casa.add_edge(3, "quincho", "patio")
casa.add_edge(3, "quincho", "cocina")

casa.add_edge(4, "sala de estar", "baño 1")
casa.add_edge(4, "sala de estar", "terraza")

casa.add_edge(1, "habitacion 1", "terraza")
casa.add_edge(3, "habitacion 1", "habitacion 2")


casa.add_edge(4, "habitacion 2", "terraza")
casa.add_edge(1, "habitacion 2", "baño 2")

# C)
arbol_exp_min = casa.kruskal("cocina")

# print(arbol_exp_min)


def MST_to_triplets_list(mst: str):
    result = []
    for i in mst.split(";"):
        result.append(i.split("-"))
    return result

# mst_como_lista = MST_to_triplets_list(arbol_exp_min)
# print(mst_como_lista)

def count_cost_mst(mst: str):
    parsed_mst = MST_to_triplets_list(mst)
    count = 0

    for i in parsed_mst:
        count += int(i[2])
    
    return count

metros_cable = count_cost_mst(arbol_exp_min)
print (f"Para conectar todos los ambientes de la casa se nececitaran {metros_cable}m de cable")


# D)

def cost_from_origin_to_destination(grap:Graph, origin:Any, destination:Any):
    dijkstra_path = grap.dijkstra(origin)
    cost = 0
    while (dijkstra_path.size() > 0):    
        value, cost, _ = dijkstra_path.pop()
        if value == destination:
            return cost

metros_cable = cost_from_origin_to_destination(casa, "sala de estar", "habitacion 1")
print (f"Para conectar el router con el Smart Tv se nececitaran {metros_cable}m de cable")
