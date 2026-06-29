# Un centro de salud gestiona la atención de pacientes utilizando una cola. 
# De cada paciente se conoce su nombre, DNI y tipo de consulta (Consulta General, 
# Urgencia, Emergencia). Implementar los siguientes algoritmos usando únicamente 
# operaciones del TDA Cola:

# - Determinar cuántos pacientes están esperando atención para cada tipo de consulta,
#   sin perder los datos de la cola.
# - Usando operaciones de cola y pila conjuntamente, invertir el contenido de la cola
#   (el último paciente que llegó debe quedar primero).
# - Dada una cola de caracteres generados a partir de los DNI de los pacientes, 
#   eliminar de ella todas los pares que aparezcan.
# - Determinar si la secuencia de nombres de los pacientes en la cola forma un 
#   palíndromo (considerando los nombres concatenados sin espacios), utilizando operaciones de cola y pila.

from queue_ import Queue
from stack import Stack

class paciente():
    def __init__(self, nombre:str, DNI:int, tipo_consulta:str):
        self.__nombre = nombre
        self.__DNI = DNI
        self.__tipo_consulta = tipo_consulta
    
    def get_nombre(self):
        return self.__nombre
    
    def get_DNI(self):
        return self.__DNI
    
    def get_tipo_consulta(self):
        return self.__tipo_consulta
    
    def __str__(self):
        return f"[Nombre: {self.__nombre} | DNI: {self.__DNI} | Tipo: {self.__tipo_consulta}]"


# Cola de pacientes inicializada
cola_pacientes = Queue()
cola_pacientes.enqueue(paciente("Juan García", 12345678, "Consulta General"))
cola_pacientes.enqueue(paciente("María López", 87654321, "Urgencia"))
cola_pacientes.enqueue(paciente("Carlos Rodríguez", 11111111, "Consulta General"))
cola_pacientes.enqueue(paciente("Ana Martínez", 22222222, "Emergencia"))
cola_pacientes.enqueue(paciente("Pedro Fernández", 33333333, "Urgencia"))

def determinar_pacientes_por_consulta(cola:Queue, consulta:str):
    contador = 0
    for _ in range(cola.size()):
        if cola[0].get_tipo_consulta() == consulta:
            contador +=1
        cola.move_to_end()
    return contador

def invertir_cola(cola:Queue):
    stack_aux = Stack()

    while cola.size() > 0:
        stack_aux.push(cola.attention())
    while stack_aux.size() > 0:
        cola.arrive(stack_aux.pop())

def generar_cola_DNIs(cola:Queue)->Queue:
    cola_DNI = Queue()
    for _ in range(cola.size()):
        cola_DNI.arrive(cola[0].get_DNI())
        cola.move_to_end()
    return cola_DNI

def es_par(num: int)->bool:
    if type(num) == int:
        if num % 2 == 0:
            return True
        else:
            return False

# def borrar_pares_cola(cola:Queue):
#     pares=["0","2","4","6","8"]
#     for _ in range(cola.size()):
#         dni = str(cola[0])
#         for c in dni:
#             if c in pares


