#3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
# si es un palíndromo.

from stack import Stack
from queue_ import Queue
from random import randint

pila = Stack()
cola = Queue()

cola.arrive("s")
cola.arrive("a")
cola.arrive("a")
cola.arrive("s")
cola.arrive("a")
cola.arrive("a")
cola.arrive("s")



def check_palindrome(cola: Queue) -> bool:
    queue_aux = Queue()


    # Reverse
    while cola.size() > 0:
        element = cola.attention()
        queue_aux.arrive(element)
        pila.push(element)

    while pila.size() > 0:
        element = pila.pop()
        cola.arrive(element)

    # Palindrome Check
    cola.show()
    queue_aux.show()
    while cola.size() > 0:
        if cola.attention() != queue_aux.attention():
            return False
    return True

if check_palindrome(cola):
    print("La cola contiene un palindromo")
else:
    print("La cola NO contiene un palindromo")


