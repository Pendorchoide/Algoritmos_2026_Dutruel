# Grafos

## Dos tipos:
- dirigidos (tienen flechas)
- no dirigidos (tienen uniones con bidireccion)

## Tienen:

- nodos o vertices
- aristas
- peso 

## Caracteristicas

- Camino: en un grafo dirigido en un conjunto de vértices (v1, v2, v3) tal que existen los arcos del
  camino (v1-v2, v2-v3)
- Longitud del camino (cantidad de aristas de un camino entre nodos)
- Etiqueta de una arista (peso): es un valor que está asociado a la relación entre dos vértices.

# Tipos de Caminos:

-Acíclico: un grafo dirigido es acíclico si no tiene ciclos, esto implica que para cada vértice del
grafo no exista ningún camino que empiece en un vértice y termine en el mismo (un vértice
podría tener un arco a sí mismo y formar un ciclo)

- Acíclico: un grafo dirigido es acíclico si no tiene ciclos, esto implica que para cada vértice del
grafo no exista ningún camino que empiece en un vértice y termine en el mismo (un vértice
podría tener un arco a sí mismo y formar un ciclo)

- Camino hamiltoniano: es un camino que consiste en visitar todos los vértices de grafo pasando
solo una vez por cada uno, si además el primer vértices es adyacente de el último el camino también es un ciclo hamiltoniano.

- Camino euleriano: es un camino pichula que consiste en pasar por cada arista del grafo solo una vez (no importa que visite los vértices más de una vez), asimismo si el vértice de partida es el vértice de llegada
el camino es un ciclo euleriano 

## Barrido:
- de produndiad
- de amp...

## algoritmo de distra