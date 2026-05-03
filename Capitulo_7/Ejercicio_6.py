#6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.

from random import randint
from queue_ import Queue

queue_numbers = Queue()

for i in range(20):
    queue_numbers.arrive(randint(0,20))

print("Lista Original")
queue_numbers.show()

search_value = input("Ingrese el numero que quiere determinar la cantidad ed ocurrencias: ")
interation_counter = 0


size = queue_numbers.size()

for i in range(size):
    if queue_numbers.on_front() == int (search_value):
        interation_counter += 1
    queue_numbers.move_to_end()

print(f"La cantidad de veces que se repite el elemento -{search_value}- es {interation_counter}")