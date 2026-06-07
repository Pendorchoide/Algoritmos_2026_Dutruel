# Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

def mostrar_vector_atras_hacia_adelante(vector: list):
    if len(vector) == 0:
        return
    else:
        print (vector.pop())
        mostrar_vector_atras_hacia_adelante(vector)

vec = [1,2,3,4]

mostrar_vector_atras_hacia_adelante(vec)