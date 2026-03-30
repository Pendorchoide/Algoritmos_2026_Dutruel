#  Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
#  número dado

def Fibonachi(num:int)->int:
    """Devuelve el valor en la secuencia Fibonacci para un número dado"""
    if num == 0 or num == 1:
        return num
    else:
        return Fibonachi(num-1) + Fibonachi(num-2)
    
fibValue = Fibonachi(int(input("Ingrese un número entero positivo para conocer su valor en la sec. Fib: ")))

print('El valor en la Sec. Fib. para el número ingresado es: ', fibValue)