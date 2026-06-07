# 6. Leer una palabra y visualizarla en forma inversa.

from stack import Stack



def mostrar_palabra_invertida(palabra: str)->str:
    p_aux = Stack()
    respone = ""

    for i in range(len(palabra)):
        p_aux.push(palabra[i])

    while p_aux.size() > 0:
        respone += p_aux.pop() 

    return respone

print(mostrar_palabra_invertida("Gato"))