# 21. Dada una lista de valores ordenadas, desarrollar un algoritmo que modifque el método de
# búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado
# está o no en dicha lista

from typing import Any

lista_1 = [1,2,3,4,5,6]

def busqueda_bin_rec(l: list[Any], buscado: Any):

    def implementacion(l: list[Any], buscado: Any, first= 0, last = len(l)):
        med = (first + last) // 2 

        if (first > last):
            return False
        
        if med == buscado:
            return True
        elif med < buscado:
            new_first = med + 1
            return implementacion(l, buscado, new_first, last)
        else:
            new_last = med - 1
            return implementacion(l, buscado, first, new_last)
    
    return implementacion(l,buscado)


print (busqueda_bin_rec(lista_1,7))