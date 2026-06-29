# Se tiene un vector de enteros cargado previamente con valores no ordenados. Implementar las siguientes funciones recursivas en Python:

# Calcular la suma de todos los dígitos de cada número del vector, sin convertir los valores a cadena de texto.
# Determinar si un valor dado se encuentra en el vector mediante búsqueda secuencial con centinela implementada de forma recursiva. La función debe devolver True o False.
# Mostrar los elementos del vector de atrás hacia adelante, sin utilizar ciclos ni estructuras auxiliares.
# Calcular el Máximo Común Divisor (MCD) de todos los elementos del vector aplicando el algoritmo de Euclides de forma recursiva.

from random import randint

vector = []

for _ in range (25):
    vector.append(randint(-10,10))

def sumar_digitos(vector:list[int])->int:
    if len(vector) == 0:
        return 0
    else:
        return vector[0] + sumar_digitos(vector[1:])
    
def busqueda_lineal(vector:list[int], buscado)->bool:
    if len(vector) == 0:
        return False
    if vector[0] == buscado:
        return True
    else:
        return busqueda_lineal(vector[1:], buscado)
    

def mostrar_al_reves(vector:list):
    if len(vector) == 1:
        return vector[0]
    else:
        return f"{mostrar_al_reves(vector[1:])}, {vector[0]}"


print(vector)

print(sumar_digitos(vector))

print(busqueda_lineal(vector,0))

print(mostrar_al_reves(vector))