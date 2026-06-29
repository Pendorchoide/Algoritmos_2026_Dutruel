# 12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
# ni métodos de ordenamiento

from queue_ import Queue

cola_1 = Queue()
cola_2 = Queue()

for i in range(10):
    if i%2 == 0:
        cola_1.arrive(i)
    else:
        cola_2.arrive(i)

cola_2.arrive(12)
cola_2.arrive(15)
cola_1.arrive(39)
cola_2.arrive(39)




def unir_colas(c1: Queue, c2:Queue)->Queue:
    nueva_cola = Queue()
    while c1.size() > 0 and c2.size() > 0:
        if c1.on_front() < c2.on_front():
            nueva_cola.arrive(c1.attention())
        else:
            nueva_cola.arrive(c2.attention())
    while c1.size() > 0:
        nueva_cola.arrive(c1.attention())

    while c2.size() > 0:
        nueva_cola.arrive(c2.attention())


    return nueva_cola



print("Cola 1")
cola_1.show()

print("")
print("Cola 2")
cola_2.show()

print("")
print("Cola 1-2")
unir_colas(cola_1,cola_2).show()

