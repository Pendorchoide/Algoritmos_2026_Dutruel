# 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
#   a. concatenar dos listas, una atrás de la otra;
#   b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
#   c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#   d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

from list_ import List

lista_A = List()
lista_B = List()
lista_C = List()


for i in range(10):
    lista_A.append(i)
for i in range(ord("a"),ord("f")):
    lista_B.append(chr(i))
for i in range(5,15):
    lista_C.append(i)

def concatenar_listas(lista_1:List, lista_2:List)->List:
    lista_resultante = List()
    i = 0
    while i< lista_1.size():
        lista_resultante.append(lista_1[i])
        i+=1
    
    i = 0
    while i< lista_2.size():
        lista_resultante.append(lista_2[i])
        i+=1

    return lista_resultante

def concatenar_listas_sin_repetidos(lista_1:List, lista_2:List)->List:
    lista_resultante = List()
    i = 0
    while i< lista_1.size():
        lista_resultante.append(lista_1[i])
        i+=1
    
    i = 0
    while i< lista_2.size():
        if (lista_2[i] not in lista_resultante):
            lista_resultante.append(lista_2[i])
        i+=1

    return lista_resultante

def contar_interseccion(lista_1:List, lista_2:List)->int:
    contador = 0
    i = 0
    while i< lista_2.size():
        if lista_2[i] in lista_1:
            contador += 1
    return contador


def mostrar_y_eliminar(lista:List):
    while lista.size()>0:
        print(lista.delete_value(lista[0]))


print("Lista A")
lista_A.show()
print("")

print("Lista B")
lista_B.show()
print("")

print("Lista C")
lista_C.show()
print("")


print("Lista A U B")
concatenar_listas(lista_A,lista_B).show()
print("")

print("Lista A U C (sin repetidos)")
concatenar_listas_sin_repetidos(lista_A,lista_C).show()
print("")

print("Contenido lista A")
mostrar_y_eliminar(lista_A)

print("Contenido lista B")
mostrar_y_eliminar(lista_B)

print("Listas Vacias (prueba)")
lista_A.show()
lista_B.show()
