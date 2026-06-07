#11. Dada una pila de letras determinar cuántas vocales contiene.

from stack import Stack
from random import randint

letras = Stack()

for i in range(10):
    letras.push(chr(randint(ord("a"),ord("z"))))

print("Pila de letras")
letras.show()

def contador_de_vocales(pila: Stack):
    vocales = ["a","e","i","o","u"]
    counter = 0
    while pila.size() > 0:
        if pila.pop() in vocales:
            counter +=1
    return counter

print(contador_de_vocales(letras))
