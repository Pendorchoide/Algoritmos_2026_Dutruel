# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
#  a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
#  b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#  c) mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
#  d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
#  e) mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
#  f) mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
#  g) determinar cuantos Pokémons tienen megaevolucion.
#  h) determinar cuantos Pokémons tiene forma gigamax.
#  cargue al menos 100 Pokémons.

from pokemon_data import pokemons
from tree import BinaryTree
from queue_ import Queue

class Pokemon():

    def __init__(self, number: int, name: str, types: list, weaknesses: list, mega: bool, gigamax: bool):
        self.__name = name
        self.__number = number
        self.__types = types
        self.__weaknesses = weaknesses
        self.__mega = mega
        self.__gigamax = gigamax

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_types(self) -> list:
        return self.__types

    def get_weaknesses(self) -> list:
        return self.__weaknesses

    def has_mega_evolution(self):
        return self.__mega

    def has_gigamax_form(self):
        return self.__gigamax

    def set_name(self, name: str):
        self.__name = name

    def set_number(self, number: int):
        self.__number = number

    def set_types(self, types: list):
        self.__types = types

    def set_weaknesses(self, weaknesses: list):
        self.__weaknesses = weaknesses

    def set_mega(self, mega: bool):
        self.__mega = mega

    def set_gigamax(self, gigamax: bool):
        self.__gigamax = gigamax

    def __str__(self):
        return f"Nombre: {self.__name}, Número: {self.__number}, Tipos: {self.__types}, Debilidades: {self.__weaknesses}, Mega Evolución: {self.__mega}, Forma Gigamax: {self.__gigamax}"

list_random_pokemons = pokemons

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()
pokemons_by_type = {} 

# A) Carga de los arboles

for pokemon in list_random_pokemons:
    poke = Pokemon(pokemon['number'], pokemon['name'], pokemon['types'], pokemon['weaknesses'], pokemon['mega'], pokemon['gigamax'])
    arbol_nombre.insert_node(poke.get_name(), poke)
    arbol_numero.insert_node(poke.get_number(), poke)
    
    for pokemon_type in poke.get_types():
        type_key = pokemon_type.casefold()
        if type_key not in pokemons_by_type:
            pokemons_by_type[type_key] = []
        pokemons_by_type[type_key].append(poke)

for type_key, pokemon_list in pokemons_by_type.items():
    arbol_tipo.insert_node(type_key, pokemon_list)  # los nodos del árbol de tipo contendrán listas de Pokémons que pertenecen a ese tipo


# B) Mostrar todos los datos de un Pokémon a partir de su número y nombre

def proxy_search(tree:BinaryTree, prefix: str):
    matches = []

    def __proxy_search(root, prefix):
        if root is None:
            return

        __proxy_search(root.left, prefix)
        if prefix in root.value.casefold():
            matches.append(root)
        __proxy_search(root.right, prefix)

    __proxy_search(tree.root, prefix.casefold())
    return matches

def show_pokemon_by_number(tree: BinaryTree, number: int):
    node = tree.search(number)
    if node is not None:
        pokemon = node.other_values
        print(pokemon)
    else:
        print("No se encontró el Pokémon con ese número.")

def show_pokemon_by_name(tree: BinaryTree, name_prefix: str):
    nodes = proxy_search(tree, name_prefix)
    if nodes:
        for node in nodes:
            print(node.other_values)
    else:
        print("No se encontró ningún Pokémon que coincida con ese texto.")

print("Mostrar Pokémon con número 3:")
show_pokemon_by_number(arbol_numero, 3) 
print("\nMostrar Pokémon con número 25:")
show_pokemon_by_number(arbol_numero, 25) 
print("\nMostrar Pokémon cuyo nombre contiene 'bul':")
show_pokemon_by_name(arbol_nombre, "um")  
print("\nMostrar Pokémon cuyo nombre contiene 'um':")
show_pokemon_by_name(arbol_nombre, "um") 

# C) Mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico

def show_pokemons_by_type(tree: BinaryTree, type: str):
    node = tree.search(type.casefold())
    if node is None:
        print(f"No se encontró el tipo {type}.")
        return
    for pokemon in node.other_values:
        print(pokemon.get_name())

print("\nPokémons de tipo fuego:")
show_pokemons_by_type(arbol_tipo, "fuego")  # Mostrar Pokémons de tipo fuego
print("\nPokémons de tipo fantasma:")
show_pokemons_by_type(arbol_tipo, "fantasma")  # Mostrar Pokémons de tipo fantasma
print("\nPokémons de tipo acero:")
show_pokemons_by_type(arbol_tipo, "acero")  # Mostrar Pokémons de tipo acero
print("\nPokémons de tipo eléctrico:")
show_pokemons_by_type(arbol_tipo, "eléctrico")  # Mostrar Pokémons de tipo eléctrico


# D) Listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre

# Se aprovechan los algoritmos de recorrido inorden y por nivel ya implementados en la clase BinaryTree con una modificacion para mostrar los datos de los Pokémons en lugar de solo el valor del nodo.

def show_pokemons_in_order_by_number(tree: BinaryTree):
    def __inorder(root):
        if root is None:
            return
        __inorder(root.left)
        poke = root.other_values
        print(f"Número: {poke.get_number()}, Nombre: {poke.get_name()}")
        __inorder(root.right)

    __inorder(tree.root)

def show_pokemons_in_order_by_name(tree: BinaryTree):
    def __inorder(root):
        if root is None:
            return
        __inorder(root.left)
        poke = root.other_values
        print(f"Nombre: {poke.get_name()}, Número: {poke.get_number()}")
        __inorder(root.right)

    __inorder(tree.root)

def show_pokemons_by_level(tree: BinaryTree):
        pendings = Queue()

        if tree.root is not None:
            pendings.arrive(tree.root)

            lvl = 0
            while(pendings.size()>0):
                print(f"Nivel {lvl}: ")

                for i in range(pendings.size()):
                    node = pendings.attention()
                    print(f"    Nombre: {node.other_values.get_name()}, Número: {node.other_values.get_number()}")
                    if node.left is not None:
                        pendings.arrive(node.left)
                    if node.right is not None:
                        pendings.arrive(node.right)
                lvl += 1
                

print("\nListado en orden ascendente por número:")
show_pokemons_in_order_by_number(arbol_numero)  # Listado en orden ascendente por número
print("\nListado en orden ascendente por nombre:")
show_pokemons_in_order_by_name(arbol_nombre)  # Listado en orden ascendente por nombre

print("\nListado por nivel por nombre:")
show_pokemons_by_level(arbol_nombre)  # Listado por nivel por nombre

# E) Mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum

def show_pokemons_weak_against(tree: BinaryTree, pokemon_name: str):
    target = tree.search(pokemon_name)
    if target is None:
        print(f"No se encontró el Pokémon {pokemon_name}.")
        return
    target_types = {pokemon_type.casefold() for pokemon_type in target.other_values.get_types()}

    def __inorder(root):
        if root is None:
            return
        __inorder(root.left)
        weaknesses = {weakness.casefold() for weakness in root.other_values.get_weaknesses()}
        if target_types & weaknesses:
            print(root.other_values.get_name())
        __inorder(root.right)

    __inorder(tree.root)


print("\nPokémons débiles frente a Jolteon:")
show_pokemons_weak_against(arbol_nombre, "Jolteon")
print("\nPokémons débiles frente a Lycanroc:")
show_pokemons_weak_against(arbol_nombre, "Lycanroc")
print("\nPokémons débiles frente a Tyrantrum:")
show_pokemons_weak_against(arbol_nombre, "Tyrantrum")

# F) Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo

def show_pokemon_types(tree: BinaryTree):
    def __inorder(root):
        if root is None:
            return
        __inorder(root.left)
        print(f"Tipo: {root.value.capitalize()}, Cantidad: {len(root.other_values)}")
        __inorder(root.right)

    __inorder(tree.root)

print("\nTipos de Pokémons y cantidad de cada tipo:")
show_pokemon_types(arbol_tipo)


# G) Determinar cuantos Pokémons tienen megaevolucion

def count_pokemons_with_mega(tree: BinaryTree):
    def __count(root):
        if root is None:
            return 0
        count = 1 if root.other_values.has_mega_evolution() else 0
        return count + __count(root.left) + __count(root.right)

    return __count(tree.root)

print(f"\nCantidad de Pokémons con megaevolución: {count_pokemons_with_mega(arbol_nombre)}")

# H) Determinar cuantos Pokémons tienen forma gigamax

def count_pokemons_with_gigamax(tree: BinaryTree):
    def __count(root):
        if root is None:
            return 0
        count = 1 if root.other_values.has_gigamax_form() else 0
        return count + __count(root.left) + __count(root.right)

    return __count(tree.root)

print(f"\nCantidad de Pokémons con forma gigamax: {count_pokemons_with_gigamax(arbol_nombre)}")