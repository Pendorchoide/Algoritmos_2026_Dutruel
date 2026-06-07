# Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
# número entero.

def MCD_euclides(a:int, b:int)->int:
    """Devuelve el MCD entre dos numeros enteros a y b mediante el algoritmo de Euclides
        Args:
        a: primer número entero
        b: segundo número entero
        returns:
        Maximo comun divisor entre a y b
    """
    r = a % b
    if r == 0:
        return b
    else:
        return MCD_euclides(b,r)
    

print(MCD_euclides(120,30))