# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
#   a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#   queden más objetos en la mochila;
#   
#   b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios 
#   sacar para encontrarlo;
#   
#   c. Utilizar un vector para representar la mochila.


back_pack_1 = ["pierna de C-3PO","comida","sable de luz","comlink"]
back_pack_2 = ["pierna de C-3PO","comida","máscara de Mandalore","comlink","piedras"]
back_pack_3 = ["sable de luz","pierna de C-3PO","comida","máscara de Mandalore","comlink","piedras"]
back_pack_4 = []

def usar_la_fuerza(back_pack:list,object_counter:int = 0):
    """Simula a un Jedi sacando objetos de su mochila para encontrar un sable de luz.
    Args:
        back_pack (list): La mochila del Jedi.
        object_counter (int, opcional): Contador de objetos sacados de la mochila. Por defecto 0.    
    """
    if len(back_pack) == 0:
        print("Mala suerte, no se encontro ningún sable de luz en la mochila")
    else:
        current_object = back_pack.pop()
        if current_object == "sable de luz":
            print("¡Se ha encontrado un sable de luz!, se sacaron ",object_counter," objetos antes de conseguirlo")
        else:
            object_counter += 1
            usar_la_fuerza(back_pack,object_counter)


print("Mochila 1:")
usar_la_fuerza(back_pack_1)

print("Mochila 2:")
usar_la_fuerza(back_pack_2)

print("Mochila 3:")
usar_la_fuerza(back_pack_3)

print("Mochila 4:")
usar_la_fuerza(back_pack_4)


    
