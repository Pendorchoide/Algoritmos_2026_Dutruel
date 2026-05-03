# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
# meros pares.

from stack import Stack
from random import randint

pila = Stack()

# Generar pila
pila = Stack()

for i in range(11):
    pila.push(randint(1,10))

print("Pila original:")
pila.show()

pila_aux = Stack()

while pila.size() > 0:
    value = pila.pop()
    if value % 2 == 0:
        pila_aux.push(value)

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())
print()
print("Nueva pila:")
pila.show()