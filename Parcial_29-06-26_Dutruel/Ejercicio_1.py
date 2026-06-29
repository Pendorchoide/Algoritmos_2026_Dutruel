# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#   funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#   funcion recursiva para listar los superheroes de la lista.

from super_heroes_data import superheroes

superheroes_15 = superheroes[:15]  # 15 superheroes almacenados como diccionarios en una lista


# Descomentar el append de abajo para agregar a Capitan America a la lista
#superheroes_15.append({ "name": "Captain America", "alias": "Captain America", "real_name": "Steve Rogers", "short_bio": "A super-soldier from World War II, Captain America is a symbol of heroism, justice, and patriotism in the Marvel Universe.", "first_appearance": 1941, "is_villain": False})


def captain_america_recursive(supers: list)->bool:
    """Funcion recursiva que devuelve True si Capitan America se encuentra en la lista"""
    if len(supers) == 0:
        return False
    elif supers[0]['name'] == "Captain America":
        return True
    else:
        return captain_america_recursive(supers[1:])
    

def list_heroes(supers: list)->None:
    if len(supers) == 0:
        return
    else:
        print(supers[0]['name'])
        return list_heroes(supers[1:])

if (captain_america_recursive(superheroes_15)):
    print("Capitan America se encuentra en la lista cargada")
else:
    print("Capitan America NO se encuentra en la lista cargada")

print("")
print("Lista de Personajes")
list_heroes(superheroes_15)



    