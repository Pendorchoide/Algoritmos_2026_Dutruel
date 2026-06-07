# 8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando
# solo una cola como estructura auxiliar.

from queue_ import Queue

def agregar_cola_ordenadamente(cola: Queue, elem: int):
    cola_aux = Queue()
    introduced = False
    if cola.size() == 0:
        cola.arrive(elem)
    else:
            while cola.size() > 0 and elem > cola.on_front():
                 cola_aux.arrive(cola.attention())
            cola_aux.arrive(elem)
            while cola.size() > 0:
                 cola_aux.arrive(cola.attention())
            while cola_aux.size() > 0:
                 cola.arrive(cola_aux.attention())


cola_1 = Queue()

agregar_cola_ordenadamente(cola_1,2)
agregar_cola_ordenadamente(cola_1,4)
agregar_cola_ordenadamente(cola_1,2)
agregar_cola_ordenadamente(cola_1,1)
agregar_cola_ordenadamente(cola_1,8)
agregar_cola_ordenadamente(cola_1,3)
agregar_cola_ordenadamente(cola_1,4)

cola_1.show()
