from PriorQueue import PriorQueue

cola_de_prioridad = PriorQueue()

# A)
cola_de_prioridad.arrive("Documento-Empleado-1",1)
cola_de_prioridad.arrive("Documento-Empleado-2",1)
cola_de_prioridad.arrive("Documento-Empleado-3",1)

# B)
print("Nueva Impresion:")
print(f"Primer Documento de la cola: {cola_de_prioridad.attention()[1]}")

# C)
cola_de_prioridad.arrive("Documento-Staff-1",2)
cola_de_prioridad.arrive("Documento-Staff-2",2)

# D)
cola_de_prioridad.arrive("Documento-Gerente-1",3)

# E)
print()
print("Nueva Impresion:")
print(f"Primer Documento de la cola: {cola_de_prioridad.attention()[1]}")
print(f"Segundo Documento de la cola: {cola_de_prioridad.attention()[1]}")

# F)
cola_de_prioridad.arrive("Documento-Empleado-4",1)
cola_de_prioridad.arrive("Documento-Empleado-5",1)
cola_de_prioridad.arrive("Documento-Gerente-2",3)

# G)
print()
print("Nueva Impresion:")
cont = 1
while (cola_de_prioridad.size() > 0):
    print(f"Documento N°{cont} de la cola: {cola_de_prioridad.attention()[1]}")
    cont += 1

print()
print("Fin de la Impresion. No mas documentos en la cola")