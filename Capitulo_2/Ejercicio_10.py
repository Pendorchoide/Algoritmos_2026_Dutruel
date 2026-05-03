#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def CountDigits(num:int)->int:
    if (num // 10) == 0:
        return 1
    else:
        return CountDigits(num // 10) + 1

print("La cantidad de digitos del valor ingresado es de: ",CountDigits(int(input("Ingrese un número para contar sus digitos: "))))