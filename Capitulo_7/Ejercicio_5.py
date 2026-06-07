# 5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.

from stack import Stack
from queue_ import Queue

pila_1 = Stack()

for i in range(10):
    pila_1.push(i)

def invertir_pila_con_cola(p: Stack):
    cola_aux = Queue()

    while p.size() > 0:
        cola_aux.arrive(p.pop())

    
    while cola_aux.size() > 0:
        p.push(cola_aux.attention())

print("Pila Original")
pila_1.show()

invertir_pila_con_cola(pila_1)
print("Pila Invertida")
pila_1.show()