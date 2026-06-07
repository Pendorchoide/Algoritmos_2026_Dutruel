#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres

from list_ import List
from random import randint

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
vowels = ["a", "e", "i", "o", "u"]

characters_1 = List()

def fill_characters(characters: List):
    for i in range(10):
        characters.append(alphabet[randint(0,25)])

fill_characters(characters_1)
print("Lista original")
characters_1.show()

def delete_vowels(characters: List):
    i = 0
    while i < characters.size():
        if characters[i] in vowels:
            characters.delete_value(characters[i])
        else:
            i += 1

delete_vowels(characters_1)
print("Lista sin vocales")
characters_1.show()

