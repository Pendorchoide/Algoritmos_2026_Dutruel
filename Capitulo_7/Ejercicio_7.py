# 7. Eliminar el i-ésimo elemento después del frente de la cola.
from queue_ import Queue

def eliminar_iesimo_elemento(cola: Queue,i:int):
    for j in range(cola.size()):
        if j == i:
            cola.attention()
        else:
            cola.move_to_end()

cola_1 = Queue()

for i in range(10):
    cola_1.arrive(i)

print("Cola Original")
cola_1.show()
eliminar_iesimo_elemento(cola_1, 3)
print("Cola Sin iesimo elemento")
cola_1.show()