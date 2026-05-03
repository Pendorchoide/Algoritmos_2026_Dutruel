#Eliminar de una cola de caracteres todas las vocales que aparecen.

from random import randint
from queue_ import Queue


vowel = ["a","e","i","o","u"]
queue_letters = Queue()

for i in range (15):
    queue_letters.arrive(chr(randint(97,122)))

print("Cola Original")
queue_letters.show()

size = queue_letters.size()
for i in range (size):
    if queue_letters.on_front in vowel:
        queue_letters.attention()
    else:
        queue_letters.move_to_end()

print("Cola Sin Vocales")
queue_letters.show()
