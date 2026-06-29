# 5. Dada una lista de números enteros eliminar de estas los números primos.

from list_ import List
from random import randint

lista_num = List()

for _ in range(20):
    lista_num.append(randint(-17,17))

def es_primo(num: int)->bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # Solo revisar impares hasta la raíz cuadrada
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
    

def eliminar_primos(lista: List):
    # Iterar desde atrás para no alterar índices al eliminar
    i = lista.size() - 1
    while i >= 0:
        if es_primo(lista[i]):
            lista.delete_value(lista[i])
        i -= 1

print("Lista original")
lista_num.sort_by_criterion()
lista_num.show()


eliminar_primos(lista_num)
print("Lista sin primos")
lista_num.show()


