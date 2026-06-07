# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.

from stack import Stack

def ingresar_ordenadamente(pila:Stack, element:int):
    p_aux = Stack()

    if pila.size() == 0:
        pila.push(element)
    else:
        if element >= pila.top_of():
            pila.push(element)
        else:
            while pila.top_of() > element:
                p_aux.push(pila.pop())
            pila.push(element)
            while p_aux.size() > 0:
                pila.push(p_aux.pop())


pila_nums = Stack()

ingresar_ordenadamente(pila_nums,1)
ingresar_ordenadamente(pila_nums,3)
ingresar_ordenadamente(pila_nums,2)
ingresar_ordenadamente(pila_nums,6)
ingresar_ordenadamente(pila_nums,7)
ingresar_ordenadamente(pila_nums,3)

pila_nums.show()

