from graph import Graph
from stack import Stack
from typing import Any
# A)
class Equipo:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return (f"Equipo: {self.__nombre} | Tipo: {self.__tipo}") 


red_de_equipos = Graph(False)

# Carga de datos

e_ubuntu = Equipo("Ubuntu", "PC")
e_impresora = Equipo("Impresora","Impresora")
e_switch_1 = Equipo("Switch 1","Switch")
e_mint = Equipo("Mint","PC")
e_debian = Equipo("Debian","Notebook")
e_router_1 = Equipo("Router 1","Router")
e_router_2 = Equipo("Router 2","Router")
e_router_3 = Equipo("Router 3","Router")
e_red_hat = Equipo("Red Hat","Notebook")
e_guarani = Equipo("Guarani","Servidor")
e_manjaro = Equipo("Manjaro","PC")
e_fedora = Equipo("Fedora","PC")
e_arch = Equipo("Arch","Notebook")
e_parrot = Equipo("Parrot","PC")
e_switch_2 = Equipo("Switch 2","Switch")
e_mongoDB = Equipo("MongoDB","Servidor")

red_de_equipos.add_vertex("Ubuntu", e_ubuntu)
red_de_equipos.add_vertex("Impresora", e_impresora)
red_de_equipos.add_vertex("Switch 1", e_switch_1)
red_de_equipos.add_vertex("Mint", e_mint)
red_de_equipos.add_vertex("Debian", e_debian)
red_de_equipos.add_vertex("Router 1", e_router_1)
red_de_equipos.add_vertex("Router 2", e_router_2)
red_de_equipos.add_vertex("Router 3", e_router_3)
red_de_equipos.add_vertex("Red Hat", e_red_hat)
red_de_equipos.add_vertex("Guarani", e_guarani)
red_de_equipos.add_vertex("Manjaro", e_manjaro)
red_de_equipos.add_vertex("Fedora", e_fedora)
red_de_equipos.add_vertex("Arch", e_arch)
red_de_equipos.add_vertex("Parrot", e_parrot)
red_de_equipos.add_vertex("Switch 2", e_switch_2)
red_de_equipos.add_vertex("MongoDB", e_mongoDB)

red_de_equipos.add_edge(17,"Switch 1","Debian")
red_de_equipos.add_edge(18,"Switch 1","Ubuntu")
red_de_equipos.add_edge(22,"Switch 1","Impresora")
red_de_equipos.add_edge(80,"Switch 1","Mint")

red_de_equipos.add_edge(29,"Router 1","Switch 1")

red_de_equipos.add_edge(37,"Router 1","Router 2")
red_de_equipos.add_edge(43,"Router 1","Router 3")
red_de_equipos.add_edge(50,"Router 2","Router 3")

red_de_equipos.add_edge(25,"Router 2","Red Hat")
red_de_equipos.add_edge(9,"Router 2","Guarani")

red_de_equipos.add_edge(61,"Router 3","Switch 2")

red_de_equipos.add_edge(40,"Switch 2","Manjaro")
red_de_equipos.add_edge(12,"Switch 2","Parrot")
red_de_equipos.add_edge(5,"Switch 2","MongoDB")
red_de_equipos.add_edge(56,"Switch 2","Arch")
red_de_equipos.add_edge(3,"Switch 2","Fedora")


# B)

# Red Hat
origin = "Red Hat"
print(f"\nBarrido de Profundidad {origin}\n")
red_de_equipos.deep_show(origin)
print(f"\nBarrido de Amplitud {origin}\n")
red_de_equipos.amplitude_show(origin)
# Debian
origin = "Debian"
print(f"\nBarrido de Profundidad {origin}\n")
red_de_equipos.deep_show(origin)
print(f"\nBarrido de Amplitud {origin}\n")
red_de_equipos.amplitude_show(origin)
# Arch
origin = "Arch"
print(f"\nBarrido de Profundidad {origin}\n")
red_de_equipos.deep_show(origin)
print(f"\nBarrido de Amplitud {origin}\n")
red_de_equipos.amplitude_show(origin)

# C)

def find_path_dijkstra(paths: Stack, origin: Any, destination: Any):
    target = destination
    path = []

    while(paths.size() > 0):
        if (paths.top_of()[0] != target):
            paths.pop()
        else:
            edge = paths.pop()
            path.append(edge[0])
            target = edge[2]

    path.reverse()
    return path

# Camino mas corto desde Manjaro

origen = "Manjaro"
destino = "Impresora"
print(f"Camino mas corto desde {origen} a {destino}")
todos_los_caminos = red_de_equipos.dijkstra(origen)
# todos_los_caminos.show()

camino_deseado = find_path_dijkstra(todos_los_caminos, origen, destino)
print(camino_deseado)
print()

# Camino mas corto desde Red Hat

origen = "Red Hat"
destino = "Impresora"
print(f"Camino mas corto desde {origen} a {destino}")
todos_los_caminos = red_de_equipos.dijkstra(origen)
# todos_los_caminos.show()

camino_deseado = find_path_dijkstra(todos_los_caminos, origen, destino)
print(camino_deseado)
print()

# Camino mas corto desde Fedora
origen = "Fedora"
destino = "Impresora"
print(f"Camino mas corto desde {origen} a {destino}")
todos_los_caminos = red_de_equipos.dijkstra(origen)
# todos_los_caminos.show()

camino_deseado = find_path_dijkstra(todos_los_caminos, origen, destino)
print(camino_deseado)
print()

# D)

arbol_exp_min = red_de_equipos.kruskal("Red Hat")
print(arbol_exp_min)

# E)

def find_nearest_node_from_type(graph: Graph, paths: Stack, type: str):
    aux_stack = Stack()
    while(paths.size()>0):
        aux_stack.push(paths.pop())

    while (aux_stack.size()> 0):
        node = aux_stack.pop()[0]
        pos = graph.search(node, "value")
        if (graph[pos]).other_values.get_tipo() == type:
            return node
        
origen = "Guarani"
tipo = "PC"
todos_los_caminos = red_de_equipos.dijkstra(origen)

# todos_los_caminos.show()
print()
print(f"Equipo de tipo {tipo} mas cercano a {origen}:")

print(find_nearest_node_from_type(red_de_equipos, todos_los_caminos, tipo))

# F)

def cost_from_origin_to_destination(grap:Graph, origin:Any, destination:Any):
    dijkstra_path = grap.dijkstra(origin)
    cost = 0
    while (dijkstra_path.size() > 0):    
        value, cost, _ = dijkstra_path.pop()
        if value == destination:
            return cost
                
    

debian_dist = cost_from_origin_to_destination(red_de_equipos, "MongoDB", "Debian")
ubuntu_dist = cost_from_origin_to_destination(red_de_equipos, "MongoDB", "Ubuntu")
mint_dist = cost_from_origin_to_destination(red_de_equipos, "MongoDB", "Mint")

if debian_dist <= ubuntu_dist and debian_dist <= mint_dist:
    print(f"El camino mas corto es desde Debian con un peso de {debian_dist}")
elif ubuntu_dist <= debian_dist and ubuntu_dist <= mint_dist:
    print(f"El camino mas corto es desde Ubuntu con un peso de {ubuntu_dist}")
else:
    print(f"El camino mas corto es desde Mint con un peso de {mint_dist}")

# G)

red_de_equipos.add_edge(67, "Impresora", "Router 2")
red_de_equipos.delete_edge("Impresora", "Switch 1")

# Red Hat
origin = "Red Hat"
print(f"\nBarrido de Profundidad {origin}\n")
red_de_equipos.deep_show(origin)
print(f"\nBarrido de Amplitud {origin}\n")
red_de_equipos.amplitude_show(origin)
# Debian
origin = "Debian"
print(f"\nBarrido de Profundidad {origin}\n")
red_de_equipos.deep_show(origin)
print(f"\nBarrido de Amplitud {origin}\n")
red_de_equipos.amplitude_show(origin)
# Arch
origin = "Arch"
print(f"\nBarrido de Profundidad {origin}\n")
red_de_equipos.deep_show(origin)
print(f"\nBarrido de Amplitud {origin}\n")
red_de_equipos.amplitude_show(origin)