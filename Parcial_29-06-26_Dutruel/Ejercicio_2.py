# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
#     a) Listado ordenado de manera ascendente por nombre de los personajes.
#     b) Determinar en que posicion esta The Thing y Rocket Raccoon.
#     c) Listar todos los villanos de la lista.
#     d) Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#     e) Listar los superheores que comienzan con  Bl, G, My, y W.
#     f) Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#     g) Listado de superheroes ordenados por fecha de aparación.
#     h) Modificar el nombre real de Ant Man a Scott Lang.
#     i) Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#     j) Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue
from stack import Stack

class Superheroe:
    def __init__(self, name:str, alias:str, real_name:str, short_bio:str, first_appearance: int, is_villain:bool):
        self.__name = name
        self.__alias = alias
        self.__real_name = real_name
        self.__short_bio = short_bio
        self.__first_appearance = first_appearance
        self.__is_villain = is_villain

    def get_name(self)->str:
        return self.__name
    
    def get_real_name(self)->str:
        return self.__real_name
    
    def set_real_name(self, new_real_name:str):
        self.__real_name = new_real_name

    def get_first_appearance(self)-> int:
        return self.__first_appearance
    
    def get_short_bio(self)->str:
        return self.__short_bio

    def get_is_villain(self)->bool:
        return self.__is_villain
    
    def __str__(self):
        return(f"name: {self.__name} | real name: {self.__real_name} | alias: {self.__alias} | short_bio: {self.__short_bio} | first_appearance: {self.__first_appearance}, is_villain: {self.__is_villain}")

superheroes_list = List()

for heroe in superheroes:
    superheroes_list.append(
        Superheroe(heroe['name'], heroe['alias'], heroe['real_name'], heroe['short_bio'], heroe['first_appearance'], heroe['is_villain'])
    )


#     a) Listado ordenado de manera ascendente por nombre de los personajes.

def by_name(item: Superheroe):
    return item.get_name()

superheroes_list.add_criterion("name",by_name)

def list_order_by_name(supers: List):
    supers.sort_by_criterion("name")
    for heroe in supers:
        print(heroe.get_name())

print("Ejercico a")
list_order_by_name(superheroes_list)
print("")

#     b) Determinar en que posicion esta The Thing y Rocket Raccoon.

def heroe_position(supers: List, name: str)->int:
    return supers.search(name,"name")

print("Ejercico B")

print(f"Posicion de Rocket Raccoon en la lista: {heroe_position(superheroes_list,"Rocket Raccoon")}")
print(f"Posicion de The Thing en la lista: {heroe_position(superheroes_list,"The Thing")}")
print("")


#     c) Listar todos los villanos de la lista.

def list_villains(characters: List)-> None:
    for i in range(characters.size()):
        if characters[i].get_is_villain():
            print (characters[i].get_name())

print("Ejercico C")
list_villains(superheroes_list)
print("")

#     d) Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

def pre_1980_villains(characters: List):
    aux_queue = Queue()
    for i in range(characters.size()):
        if characters[i].get_is_villain():
            aux_queue.arrive(characters[i])
    
    for i in range(aux_queue.size()):
        char = aux_queue.on_front()
        if char.get_first_appearance() < 1980:
            print(f"Name: {char.get_name()} | First Appearance: {char.get_first_appearance()}")
        aux_queue.move_to_end()

print("Ejercico D")
pre_1980_villains(superheroes_list)
print("")

#     e) Listar los superheores que comienzan con  Bl, G, My, y W.

def list_by_initial(characters: List, initial:str)->None:
    for i in range(characters.size()):
        if characters[i].get_name().startswith(initial):
            print(characters[i].get_name())

print("Ejercico E")
list_by_initial(superheroes_list,"Bl")
list_by_initial(superheroes_list,"G")
list_by_initial(superheroes_list,"My")
list_by_initial(superheroes_list,"W")
print("")

#     f) Listado de personajes ordenado por nombre real de manera ascendente de los personajes.

def by_real_name(item: Superheroe):
    nombre_real = item.get_real_name()
    return nombre_real if nombre_real is not None else ""

superheroes_list.add_criterion("real_name", by_real_name)

def list_order_by_real_name(supers: List):
    supers.sort_by_criterion("real_name")
    for heroe in supers:
        real_name = heroe.get_real_name()
        if(real_name):
            print(real_name)


print("Ejercico f")
list_order_by_real_name(superheroes_list)
print("")

#     g) Listado de superheroes ordenados por fecha de aparación.

def by_first_appearance(item: Superheroe):
    return item.get_first_appearance()

superheroes_list.add_criterion("first_appearance", by_first_appearance)

def list_by_first_appearance(characters: List)->None:
    characters.sort_by_criterion("first_appearance")
    for i in range(characters.size()):
        char = characters[i]
        print(f"Name: {char.get_name()} | First Appearance: {char.get_first_appearance()}")

print("Ejercico g")
list_by_first_appearance(superheroes_list)
print("")

#     h) Modificar el nombre real de Ant Man a Scott Lang.

def modify_real_name(characters:List, hero_name:str, new_real_name:str):
    pos = characters.search(hero_name, "name")
    characters[pos].set_real_name(new_real_name)

    print(f"Cambio hecho: name: {characters[pos].get_name()} | real name: {characters[pos].get_real_name()}")


print("Ejercico h")
modify_real_name(superheroes_list, "Ant Man", "Scott Lang")
print("")


#     i) Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

def list_by_word_in_bio(characters:List, word:str):
    for i in range(characters.size()):
        if word in characters[i].get_short_bio():
            char = characters[i]
            print(f"name: {char.get_name()} | short bio: {char.get_short_bio()}")

print("Ejercico i")
list_by_word_in_bio(superheroes_list, "time-traveling")
list_by_word_in_bio(superheroes_list, "suit")
print("")

#     j) Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

def eliminate_characters(characters: List, name: str):

    char = characters.delete_value(name,"name")
    if char:
        print(f"Se elimino correctamente a {char}")
    else:
        print(f"No se encontro a {name} en la lista")

print("Ejercico j")
print("")
eliminate_characters(superheroes_list, "Electro")
print("")
eliminate_characters(superheroes_list, "Baron Zemo")

