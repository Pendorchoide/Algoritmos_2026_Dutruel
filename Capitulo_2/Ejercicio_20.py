# Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
# manera recursiva, y permita determinar si un valor dado está o no en dicha lista.
from typing import Any

lista = [1,2,3,4,5,6]



def busqueda_secuencial_con_centinela(lista: list, valor: Any) -> bool:
    if len(lista) == 0:
        return False
    elif lista[0] == valor:
        return True
    else:
        return busqueda_secuencial_con_centinela(lista[1:], valor)

print(busqueda_secuencial_con_centinela(lista, 1))
print(busqueda_secuencial_con_centinela(lista, 10))
