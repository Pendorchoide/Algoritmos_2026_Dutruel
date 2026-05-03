"""
24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
    a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi
    ción uno la cima de la pila;
    b. determinar los personajes que participaron en más de 5 películas de la saga, además indi
    car la cantidad de películas en la que aparece;
    c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
"""

from stack import Stack


class Character:
    def __init__(self, name: str, movie_count: int):
        self.__name = name
        self.__movie_count = movie_count

    def get_name(self):
        return self.__name
    
    def get_movie_count(self):
        return self.__movie_count
    


    def __str__(self):
        return f"[Nombre: {self.__name}; Peliculas: {self.__movie_count}]"
    
character_stack = Stack()

character_stack.push(Character("Iron Man", 9))
character_stack.push(Character("Electro", 2))
character_stack.push(Character("Spider Man", 12))
character_stack.push(Character("Storm", 6))
character_stack.push(Character("Rocket Raccoon", 7))
character_stack.push(Character("Rogue", 4))
character_stack.push(Character("Loki", 7))
character_stack.push(Character("Dr Strange", 6))
character_stack.push(Character("Groot", 6))
character_stack.push(Character("Black Widow", 9))
character_stack.push(Character("Captain America", 2))

def find_character(stack: Stack, searched: str) -> int:
    aux_stack = Stack()
    index = 1
    position = None
    founded = False

    while (stack.size() > 0) and (not founded):
        element = stack.pop()
        aux_stack.push(element)

        if element.get_name() == searched:
           position = index
           founded = True
        index += 1
        
    while aux_stack.size() > 0:
        element = aux_stack.pop()
        stack.push(element)

    return position

def more_than_x_movies(stack: Stack, movie_threshold: int):
    aux_stack = Stack()

    while stack.size() > 0:
        element = stack.pop()
        aux_stack.push(element)

        if element.get_movie_count() > movie_threshold:
            print(f"    - {element.get_name()} aparecio en un total de {element.get_movie_count()} peliculas")

    while aux_stack.size() > 0:
        element = aux_stack.pop()
        stack.push(element)


def black_widow_analyser(stack: Stack):

    aux_stack = Stack()
    founded = False

    while stack.size() > 0:
        element = stack.pop()
        aux_stack.push(element)

        if element.get_name() == "Black Widow":
            print(f"Black Widow se encuentra en la pila. Participo en un total de {element.get_movie_count()} peliculas")
            founded = True

    while aux_stack.size() > 0:
        element = aux_stack.pop()
        stack.push(element)

    if not founded:
        print(f"Black Widow no se encuentra en la pila")


def c_d_e_initial_characters(stack: Stack):
    aux_stack = Stack()
    founded = False

    while stack.size() > 0:
        element = stack.pop()
        aux_stack.push(element)

        if element.get_name()[0] in ("C","D","E"):
            print(f"    - El personaje {element.get_name()} comienza con la letra {element.get_name()[0]}")
            founded = True

    while aux_stack.size() > 0:
        element = aux_stack.pop()
        stack.push(element)
    
    if not founded:
        print("No se encontraron personajes que comiencen con 'C', 'D' o 'E'")
character_stack.show()

print ("\n= Busqueda de Rocket Raccoon =")
character_pos = find_character(character_stack,"Rocket Raccoon")
if character_pos != None:
    print(f"Posición de Rocket Raccoon: {character_pos}")
else:
    print("El personaje buscado no se encuentra en la lista")

print ("\n= Busqueda de Groot =")
character_pos = find_character(character_stack,"Groot")
if character_pos != None:
    print(f"Posición de Groot: {character_pos}")
else:
    print("El personaje buscado no se encuentra en la lista")

print ("\n= Busqueda de Hulk =")
character_pos = find_character(character_stack,"Hulk")
if character_pos != None:
    print(f"Posición de Hulk: {character_pos}")
else:
    print("El personaje buscado no se encuentra en la lista")


print ("\n= Personajes que aparecieron en mas de 5 peliculas =")

more_than_x_movies(character_stack,5)


print ("\n= Participacion de Black Widow =")

black_widow_analyser(character_stack)

print ("\n= Personajes que comienzan con C, D o E =")

c_d_e_initial_characters(character_stack)

#print("")
#character_stack.show()



