#1. Determinar el número de ocurrencias de un determinado elemento en una pila.


from stack import Stack
from random import randint

# Generar pila
pila = Stack()

for i in range(11):
    pila.push(randint(1,10))

pila.show()

print()
searched_value = int(input("Ingrese el valor que desea buscar: "))
counter = 0

while pila.size() > 0:
    if pila.pop() == searched_value:
        counter +=1

print()
print(f"El número {searched_value} aparece un total de {counter} veces en la pila")



