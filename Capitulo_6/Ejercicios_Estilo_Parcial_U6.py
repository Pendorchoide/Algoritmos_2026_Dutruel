# Se dispone de una pila con las tareas pendientes de un proyecto de software. 
# De cada tarea se conoce su nombre, prioridad (1 = baja, 2 = media, 3 = alta) y 
# estado (Pendiente, En progreso, Bloqueada). 
# Implementar los siguientes algoritmos utilizando únicamente operaciones del TDA Pila:

# Contar cuántas tareas tienen prioridad alta, sin perder los datos de la pila original.
# Eliminar todas las tareas con estado "Bloqueada" mostrando su nombre al momento de eliminarlas.
# Insertar una nueva tarea con prioridad alta en la i-ésima posición debajo de la cima, utilizando únicamente una pila auxiliar.
# Ordenar la pila de forma creciente según prioridad, usando una única pila auxiliar como estructura extra. No se pueden utilizar métodos de ordenamiento predefinidos.

from stack import Stack

class Tarea():
    def __init__(self, nombre:str, prioridad:int, estado:str):
        self.__nombre = nombre
        self.__prioridad = prioridad
        self.__estado = estado

    def get_nombre(self):
        return self.__nombre
    
    def get_prioridad(self):
        return self.__prioridad
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado:str):
        self.__estado = estado
    
    def __str__(self):
        return f"[Nombre: {self.__nombre} | Prioridad: {self.__prioridad} | Estado: {self.__estado}]"


# Pila de tareas inicializada
pila_tareas = Stack()
pila_tareas.push(Tarea("Diseño de interfaz", 2, "Pendiente"))
pila_tareas.push(Tarea("Configurar servidor", 3, "En progreso"))
pila_tareas.push(Tarea("Testing modulo A", 3, "Bloqueada"))
pila_tareas.push(Tarea("Revisar código", 2, "Pendiente"))
pila_tareas.push(Tarea("Documentación", 1, "Pendiente"))
pila_tareas.push(Tarea("Deploy a producción", 3, "En progreso"))

def contar_prioridad_alta(pila: Stack)-> int:
    pila_aux = Stack()
    contador = 0
    while pila.size() > 0:
        if pila.top_of().get_prioridad() == 3:
            contador += 1
        pila_aux.push(pila.pop())
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    return contador
        

def eliminar_bloqueadas(pila: Stack)-> None:
    pila_aux = Stack()
    while pila.size() > 0:
        tarea = pila.pop()
        if tarea.get_estado() == "Bloqueada":
            print(f"Tarea Eliminada: {tarea}")
        else:
            pila_aux.push(tarea)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())


def insertar_tarea_iesima_pos(pila:Stack, i: int, tarea: Tarea):
    pila_aux = Stack()
    if i > pila.size():
        return
    for _ in range(i):
        pila_aux.push(pila.pop())
    pila.push(tarea)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

# def ordenar_por_prioridad(pila: Stack):
#     pila_aux = Stack()
    
#     # Procesar cada elemento de la pila original
#     while pila.size() > 0:
#         tarea = pila.pop()
        
#         # Mientras la auxiliar no esté vacía y su tope tiene mayor prioridad,
#         # devolver elementos a la original
#         while pila_aux.size() > 0 and pila_aux.top_of().get_prioridad() > tarea.get_prioridad():
#             pila.push(pila_aux.pop())
        
#         # Insertar la tarea en la posición correcta en la auxiliar
#         pila_aux.push(tarea)
    
#     # Devolver los elementos ordenados a la pila original
#     while pila_aux.size() > 0:
#         pila.push(pila_aux.pop())















def ordenar_por_prioridad(pila:Stack):
    pila_aux= Stack()
 
    while pila.size()>0:
        tarea = pila.pop()
        while pila_aux.size()>0 and tarea.get_prioridad() > pila_aux.top_of().get_prioridad():
            pila.push(pila_aux.pop())
        pila_aux.push(tarea)
    while pila_aux.size()>0:
        pila.push(pila_aux.pop())

print("Pila Original")
pila_tareas.show()
print("")

print("Cantidad Alta Prioridad:")
print(contar_prioridad_alta(pila_tareas))
print("")

print("Eliminadas:")
eliminar_bloqueadas(pila_tareas)
print("")

print("Insercion de Tarea:")
insertar_tarea_iesima_pos(pila_tareas,3,Tarea("Zawardo",2,"Pendiente"))
pila_tareas.show()
print("")

print("Orden por prioridad:")
ordenar_por_prioridad(pila_tareas)
pila_tareas.show()
print("")