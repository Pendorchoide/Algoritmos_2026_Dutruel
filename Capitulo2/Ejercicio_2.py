#  2. Implementar una función que calcule la suma de todos los números enteros comprendidos
#  entre cero y un número entero positivo dado.

def IntegerSume(num:int)->int:
    """Devuelve la suma de todos los enteros comprendidos entre 0 y un valor dado"""
    if num == 0 or num == 1:
        return 0
    else:
        return num - 1 + IntegerSume(num-1)
    
intValue = IntegerSume(int(input("Ingrese un número entero positivo para conocer la suma de todos los enteros entre este y 0: ")))

print('El valor las suma de enteros es: ', intValue)