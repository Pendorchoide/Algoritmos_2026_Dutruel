##  Implementar una función para calcular el producto de dos números enteros dados

def MultInt(num1:int,num2:int)->int:
    """Devuelve el producto entre dos enteros dados"""
    if num1 == 0 or num2 == 0:
        return 0
    else:
        return num1 + MultInt(num1,num2-1)

val1 = int(input("Ingrese el primero número que desea multiplicar: "))
val2 = int(input("Ingrese el segundo número que desea multiplicar: "))
print('El producto entre ambos números es: ', MultInt(val1,val2))