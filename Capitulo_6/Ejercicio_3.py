#3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from stack import Stack
from random import randint

pila_1 = Stack()

for i in range(10):
    pila_1.push(randint(1,10))


def reemplazar_ocurrencias(pila:Stack, elem_a_reemplazar: any, reemplazo: any):
    aux_pila = Stack()
    while pila.size() > 0:
        elem = pila.pop()
        
        if str(elem) == str(elem_a_reemplazar):
            aux_pila.push(reemplazo)
        else:
            aux_pila.push(elem)
    
    while aux_pila.size() > 0:
        elem = aux_pila.pop()
        pila.push(elem)

print("Pila Original:")
pila_1.show()
print("")
a_cambiar = input("Ingrese el elemento que desea cambiar: ")
reemp = input("Ingrese el elemento por el que quiere reemplazarlo: ")
reemplazar_ocurrencias(pila_1, a_cambiar, reemp)
print("")
print("Nueva Pila")
pila_1.show()
