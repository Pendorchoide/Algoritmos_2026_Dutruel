# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# b) hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# e) calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# f) indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph
from star_wars_data import characters, connections
from stack import Stack
from typing import Any

grafo_personajes = Graph(is_dir=False)

# A) Cargar los vértices y aristas del grafo con los personajes y las conexiones entre ellos

for character in characters:
    grafo_personajes.add_vertex(character["name"])

for connection in connections:
    grafo_personajes.add_edge(connection["weight"], connection["origin"], connection["destination"])

grafo_personajes.show()  # Mostrar el grafo de personajes y conexiones

# B) Hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia
mst_C3PO = grafo_personajes.kruskal("C3PO")
mst_Yoda = grafo_personajes.kruskal("Yoda")
mst_Leia = grafo_personajes.kruskal("Leia")

# Como nota los 3 árboles de expansión mínima son iguales, ya que el algoritmo de Kruskal genera un único árbol de expansión mínima para un grafo conexo, independientemente del vértice de inicio.
print("Árbol de expansión mínimo desde C-3PO:")
print(mst_C3PO)
print("\nÁrbol de expansión mínimo desde Yoda:")
print(mst_Yoda)
print("\nÁrbol de expansión mínimo desde Leia:")
print(mst_Leia)

# C) Determinar cuál es el número máximo de episodios que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número

def find_max_shared_episodes(graph: Graph):
    max_shared_episodes = 0
    pairs_with_max_shared_episodes = []

    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight > max_shared_episodes:
                max_shared_episodes = edge.weight
                pairs_with_max_shared_episodes = [(vertex.value, edge.destination)]
            elif edge.weight == max_shared_episodes:
                pairs_with_max_shared_episodes.append((vertex.value, edge.destination))

    return max_shared_episodes, pairs_with_max_shared_episodes

max_episodes, pairs = find_max_shared_episodes(grafo_personajes)
# Como nota, no se filtra los pares de personajes repetidos, ya que el grafo es no dirigido y cada arista se representa en ambos vértices.
print("\nNúmero máximo de episodios compartidos y pares de personajes:")
print(f"Máximo: {max_episodes}")
print("Pares:")
for pair in pairs:
    print(f"  - {pair[0]} y {pair[1]}")

# E) Calcular el camino más corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader 
# Como nota el camino más corto es considerado como el de menor peso.
def find_shortest_path_from_x_to_y(origin: Any, destination: Any):
    paths = grafo_personajes.dijkstra(origin)
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

shortest_path_C3PO_R2D2 = find_shortest_path_from_x_to_y("C3PO", "R2D2")
shortest_path_Yoda_DarthVader = find_shortest_path_from_x_to_y("Yoda", "Darth Vader")

print("\nCamino más corto desde C-3PO a R2-D2:")
print(shortest_path_C3PO_R2D2)
print("\nCamino más corto desde Yoda a Darth Vader:")
print(shortest_path_Yoda_DarthVader)

# F) Indicar qué personajes aparecieron en los nueve episodios de la saga
def find_characters_in_all_episodes(graph: Graph):
    characters_in_all_episodes = []
    for character in graph:
        for edge in character.edges:
            if edge.weight == 9:
                characters_in_all_episodes.append(character.value)
                break
    return characters_in_all_episodes

characters_in_all_episodes = find_characters_in_all_episodes(grafo_personajes)
print("\nPersonajes que aparecieron en los nueve episodios de la saga:")
print(characters_in_all_episodes)