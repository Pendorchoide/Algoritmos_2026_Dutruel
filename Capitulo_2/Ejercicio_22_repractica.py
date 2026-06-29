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

def sable_searcher(mochila: list, contador:int = 0):
    if len(mochila) == 0:
        print("No se encontro ningun sable de luz")
    elif mochila[0] == "sable de luz":
        print("Se encontro un sable de luz")
        print(f"Se sacaron {contador} objetos antes de encontrarlo")
    else:
        mochila.pop(0)
        contador += 1
        return sable_searcher(mochila, contador)

def usar_la_fuerza(mochila:list):
    sable_searcher(mochila)


usar_la_fuerza(back_pack_4)