# Determinar si una cadena de caracteres es un palíndromo.
from stack import Stack

pila = Stack()

pila.push("a")
pila.push("s")
pila.push("s")
pila.push("a")



def palindrome_check(p:Stack)-> bool:
    result = True
    p_aux = Stack()
    p_aux2 = Stack()
    while p.size() > 0:
        element = p.pop()
        p_aux.push(element)
        p_aux2.push(element)

    while p_aux2.size() > 0:
        p.push(p_aux2.pop())

    while p.size() > 0:
        if p.pop() != p_aux.pop():
            result = False

    return result


def palindrome_check_v2(p: Stack) -> bool:
    """Verifica si una pila representa un palíndromo."""
    p_aux = Stack()
    
    # Extraer la primera mitad
    for _ in range(p.size() // 2):
        p_aux.push(p.pop())
    
    # Ignorar el elemento del medio si el tamaño es impar
    if p.size() % 2 == 1:
        p.pop()
    
    # Comparar y retornar False apenas encuentre una diferencia
    while p_aux.size() > 0:
        if p_aux.pop() != p.pop():
            return False
    
    return True

#print(palindrome_check(pila))
print(palindrome_check_v2(pila))
