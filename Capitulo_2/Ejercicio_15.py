# Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
# Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
# el número a calcular su raíz.

def heron_raiz(num:int,x:float)->int:
    aproximation = 0.5 * (x + (num/x))
    if abs(x - aproximation) < 0.01:
        return aproximation
    else:
        return heron_raiz(num,aproximation)

def raiz_cuadrada_entera(num:int)->int:
    return int(heron_raiz(num,num/2))

print (raiz_cuadrada_entera(123))