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
    def __init__(self, nombre: str, apariciones: int):
        self.__nombre = nombre
        self.__apariciones = apariciones
    
    def get_nombre(self)->str:
        return self.__nombre
    
    def get_apariciones(self)->int:
        return self.__apariciones

    def __str__(self):
        return f"[nombre: {self.__nombre}, apariciones: {self.__apariciones}]"
    
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

def determinar_posicion(pila:Stack, nombre:str)->int:
    aux_stack = Stack()
    founded = False
    pos = 1
    while pila.size() > 0 and founded == False:
        character = pila.pop()
        aux_stack.push(character)
        if character.get_nombre() == nombre:
            founded = True
        else:
            pos += 1
        
    while aux_stack.size() > 0:
        pila.push(aux_stack.pop())

    if founded: return pos

def mostrar_c_d_g(pila: Stack):
    aux_stack= Stack()

    while pila.size() > 0:
        element = pila.pop()
        aux_stack.push(element)
        
        if element.get_nombre().startswith("C") or element.get_nombre().startswith("D") or element.get_nombre().startswith("G"):
            print(element)

    while aux_stack.size() > 0:
            pila.push(aux_stack.pop())
character_stack.show()

print(f"Rocket Pos: {determinar_posicion(character_stack, "Rocket Raccoon")}")
print(f"Groot Pos: {determinar_posicion(character_stack, "Groot")}")


print("")
mostrar_c_d_g(character_stack)