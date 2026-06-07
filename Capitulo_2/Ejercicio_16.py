# Implementar un función recursiva que permita obtener el valor de an en una sucesión geomé-
# trica (o progresión geométrica) con un valor a1= 2 y una razón r = -3. Además desarrollar un
# algoritmo que permita visualizar todos los valores de dicha sucesión desde a1 hasta an.

def sucecion_geometrica(n:int)->int:
    a = 2
    r = -3
    if n < 1:
        return 0
    elif n == 1:
        return a * r
    else:
        return sucecion_geometrica(n-1) * r
    
def sucecion_geometrica_listada(n:int)->int:
    a = 2
    r = -3
    if n < 1:
        return 0
    elif n == 1:
        result = a * r
        print(result)
        return result
    else:
        result = sucecion_geometrica_listada(n-1) * r
        print(result)
        return result
    

sucecion_geometrica_listada(100)