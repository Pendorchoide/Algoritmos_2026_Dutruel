# 4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos

from queue_ import Queue
from random import randint

cola = Queue()

for i in range(10):
    cola.arrive(randint(1,17))

def es_primo(num:int)->bool:
    result = True
    for i in range(2,num):
        if num % i == 0:
            result = False
    return result

print("cola Original")
cola.show()

def eliminar_primos(c: Queue):
    for _ in range(c.size()):
        if es_primo(c.on_front()):
            c.attention()
        c.move_to_end()

eliminar_primos(cola)

print("cola sin primos")
cola.show()
