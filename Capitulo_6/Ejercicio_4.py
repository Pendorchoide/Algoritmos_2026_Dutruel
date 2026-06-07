#4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra

from stack import Stack

pila = Stack()

for i in range(10):
    pila.push(i)

print("Pila original")
pila.show()

def invertir_pila(p: Stack)->Stack:   
    p_aux = Stack()
    while p.size() > 0:
        p_aux.push(p.pop())
    return p_aux

pila_invertida = invertir_pila(pila)

pila_invertida.show()