# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
# pila con nombres de dioses griegos.

from stack import Stack

dioses = Stack()

dioses.push("Zeus")
dioses.push("Hades")
dioses.push("Poseidon")
dioses.push("Hefestus")
dioses.push("Hera")
dioses.push("Apolo")
dioses.push("Afrodita")
dioses.push("Ares")
dioses.push("Dionisio")
dioses.push("Zagreo")
dioses.push("Artemisa")
dioses.push("Hermes")

def insertar_Atena_iesima_pos(p:Stack,i:int):
    p_aux = Stack()
    if i < p.size():
        for _ in range(i):  #Se considera a la cima como i=0
            p_aux.push(p.pop())
    
    p.push("Atenea")

    while p_aux.size() > 0:
        p.push(p_aux.pop())


print("Dioses 1")
dioses.show()

insertar_Atena_iesima_pos(dioses,3)

print("Dioses 2")
dioses.show()



