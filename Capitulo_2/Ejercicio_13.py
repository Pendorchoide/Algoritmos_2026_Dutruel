# Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
# de dos número entero.

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
    
def MCM_euclides(a:int, b:int)->int:
    """Devuelve el MCM entre dos numeros enteros a y b mediante el algoritmo de Euclides
        Args:
        a: primer número entero
        b: segundo número entero
        returns:
        Minimo comun Multiplo entre a y b
    """
    return abs(a * b) // MCD_euclides(a,b)

print (MCM_euclides(-2,20))