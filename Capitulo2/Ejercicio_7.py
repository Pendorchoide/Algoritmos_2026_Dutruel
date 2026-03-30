#  7. Desarrollar un algoritmo que permita calcular la siguiente serie:
#  h(n) = 1 + 1/2 + 1/3 + ... + 1/n

def HarmonicSeries(num:int)->float:
    """Da el resultado de la serie armonica iterada un numero finito de veces (num)"""
    if num == 1:
        return 1
    else:
        return HarmonicSeries(num-1) + 1/num

value = int(input("ingrese cuantas veces desea iterar la serie armónica: "))
print("La serie armonica con ", value," iteraciones es igual a ", HarmonicSeries(value))