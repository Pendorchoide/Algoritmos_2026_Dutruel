# 8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
# cartas de baraja española–,resolver las siguientes actividades:
#   a. generar las cartas del mazo de forma aleatoria;
#   b. separar la pila mazo en cuatro pilas una por cada palo;
#   c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

from stack import Stack
import random

class Carta:
    def __init__(self,valor:int,palo:str):
      self.__valor = valor
      self.__palo = palo
    
    def get_valor(self)->int:
        return self.__valor

    def get_palo(self)->str:
        return self.__palo
    
    def __str__(self):
        return f"[Valor: {self.__valor}; Palo: {self.__palo}]"
    



def mazo_pila_mezclado(m: Stack):
    palos = ["Espadas", "Oro", "Copas", "Basto"]
    mazo_aux = []

    for i in range (4):
        for j in range(1,13):
            mazo_aux.append(Carta(j,palos[i]))

    random.shuffle(mazo_aux)

    for card in mazo_aux:
        m.push(card)

def separar_por_palo(mazo:Stack,e:Stack,o:Stack,b:Stack,c:Stack):
    while mazo.size() > 0:
        match (mazo.top_of().get_palo()):
            case "Espadas": e.push(mazo.pop())
            case "Oro": o.push(mazo.pop())
            case "Basto": b.push(mazo.pop())
            case "Copas": c.push(mazo.pop())


def ordenar_pila(p: Stack):
    p_aux= Stack()
    p_aux2= Stack()
    i = 1

    while p_aux2.size() != 12:
        while p.size() > 0:
            if p.top_of().get_valor() == i:
                p_aux2.push(p.pop())
                i += 1
            else:
                p_aux.push(p.pop())
        while p_aux.size() > 0:
            p.push(p_aux.pop())
    
    while p_aux2.size() > 0:
        p.push(p_aux2.pop())










mazo = Stack()
pila_espadas = Stack()
pila_oros = Stack()
pila_bastos = Stack()
pila_copas = Stack()

mazo_pila_mezclado(mazo)

print("Mazo desordenado")
mazo.show()

separar_por_palo(mazo,pila_espadas,pila_oros,pila_bastos,pila_copas)

print("Espadas")
pila_espadas.show()
print("Oros")
pila_oros.show()
print("Bastos")
pila_bastos.show()
print("Copas")
pila_copas.show()


ordenar_pila(pila_espadas)

print("Espadas Ordenadas")
pila_espadas.show()
