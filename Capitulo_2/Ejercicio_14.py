# Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
# se puede convertir el número a cadena.

def SumaDeDigitosRecursiva(num: int) -> int:
    """Devuelve la suma de los digitos de un numero entero
        Args:
        num: numero cuyos digitos van a ser sumados

        Return:
        La suma de los digitos de num
    """
    num = abs(num)
    if num == 0:
        return 0
    else:
        return (num % 10) + SumaDeDigitosRecursiva(num // 10)
    

print(SumaDeDigitosRecursiva(123))