# Dada la siguiente defnición de sucesión recursiva, realizar una función recursiva que permita
# calcular el valor de un determinado número en dicha sucesión.

def funcion(n:int):
    if n == 1:
        return 2
    else:
        return n + (1/funcion(n - 1))    

print(funcion(5))