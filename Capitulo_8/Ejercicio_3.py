# 3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
# una que contenga los números pares y otra para los números impares.

from list_ import List
from random import randint

lista_numeros = List()

for _ in range(15):
    lista_numeros.append(randint(-20,20))

def es_par(num:int)->bool:
    if type(num) == int:
        if num % 2 == 0:
            return True
        else:
            return False
        
def dividir_pares_impares(lista_original: List,lista_pares: List,lista_impares: List):
    i = 0
    while i < lista_original.size():
        if es_par(lista_original[i]):
            lista_pares.append((lista_original[i]))
        else:
            lista_impares.append((lista_original[i]))
        i += 1




lista_p = List()
lista_i = List()

print("Lista Original")
lista_numeros.show()

dividir_pares_impares(lista_numeros,lista_p,lista_i)

print("Lista Pares")
lista_p.show()
print("Lista Impares")
lista_i.show()
