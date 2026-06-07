#7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

from stack import Stack 

def eliminar_iesimo_elemento(p:Stack, i:int):
    p_aux = Stack()

    if p.size() < i:
        print("La pila no tiene una posicion ", i)
        return

    og_size = p.size()
    while p.size() > (og_size - i):   #se considera la sima de la pila como i = 0
        p_aux.push(p.pop())

    p.pop()

    while p_aux.size() > 0:
        p.push(p_aux.pop())


pila = Stack()

for i in range(10):
    pila.push(i)

print("Primera pila")
pila.show()

eliminar_iesimo_elemento(pila,3)

print("Segunda pila")
pila.show()
    