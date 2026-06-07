# 2. Utilizando operaciones de cola y pila, invertir el contenido de una cola

from stack import Stack
from queue_ import Queue
from random import randint

pila = Stack()
cola = Queue()

for i in range(10):
    cola.arrive(randint(1,10))

print("Cola original")
cola.show()

while cola.size() > 0:
    element = cola.attention()
    pila.push(element)

while pila.size() > 0:
    element = pila.pop()
    cola.arrive(element)

print("Cola invertida")
cola.show()