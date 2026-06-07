# 9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
from queue_ import Queue
from random import randint
cola_1 = Queue()

for _ in range(10):
    cola_1.arrive(randint(-20,20))


def determinar_rango(cola:Queue)->int:
    cola_aux = Queue()
    max_elem = cola.on_front()
    min_elem = cola.on_front()

    while cola.size() > 0:
        front = cola.on_front()
        if front > max_elem:
            max_elem = front
        elif front< min_elem:
            min_elem = front

        cola_aux.arrive(cola.attention())

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
    
    return max_elem - min_elem


def contador_negativos(cola:Queue)->int:
    cola_aux = Queue()
    contador = 0

    while cola.size() > 0:
        if cola.on_front() < 0:
            contador += 1
        cola_aux.arrive(cola.attention())

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())
    
    return contador


cola_1.show()

print(f"Rango: {determinar_rango(cola_1)}")
print(f"Cantidad Negativos: {contador_negativos(cola_1)}")

