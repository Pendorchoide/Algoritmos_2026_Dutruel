# 9. Resolver el problema del factorial de un número utilizando una pila. 

from stack import Stack

def factorial_pila(n:int):
    pila = Stack()

    factorial = 1

    for i in range (1, n + 1):
        pila.push(i)

    while pila.size() > 0:
        factorial *= pila.pop()
    
    return factorial


print(factorial_pila(5))