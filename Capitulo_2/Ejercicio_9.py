# Implementar una función para calcular el logaritmo entero de número n en una base b. 

def logaritmoEntero(n: int, b:int) -> int:
    """ Devuelve el logaritmo entero de un número n en base b
    Args:
        n = argumento
        b = base
    Returns:
        int
    """
    if n < b:
        return 0
    else:
        return 1 + logaritmoEntero(n // b,b)

print(logaritmoEntero(42,3))