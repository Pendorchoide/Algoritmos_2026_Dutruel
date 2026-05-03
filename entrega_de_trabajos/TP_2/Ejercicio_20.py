# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.-

from stack import Stack
from random import randint

CARDINAL_POINTS = ["N","S","E","W","NE","SE","NW","SW"]
instruction_historial = Stack()


class Robot:
    
    def __init__(self):
        self.__x: float = 0
        self.__y: float = 0
    
    def move(self, direction, steps):
        match direction:
            case "N":
                self.__y += steps
            case "S":
                self.__y -= steps
            case "E":
                self.__x += steps
            case "W":
                self.__x -= steps

            case "NE":
                self.__y += steps / 2
                self.__x += steps / 2
            case "SE":
                self.__y -= steps / 2
                self.__x += steps / 2
            case "NW":
                self.__y += steps / 2
                self.__x -= steps / 2
            case "SW":
                self.__y -= steps / 2
                self.__x -= steps / 2

    def location(self)-> tuple[float,float]:
        return (self.__x, self.__y)
    


def generate_instructions(instruction_container: Stack):
    for i in range(10):
        instruction = (CARDINAL_POINTS[randint(0,7)], randint(1,5))  # Guarda la direccion y numero de pasos como un tuple
        instruction_historial.push(instruction)

def backward_instructions(instructions: Stack):
    aux_stack = Stack()

    while instructions.size() > 0:
        i = instructions.pop()
        i = (i[0], -i[1])       # hace que los pasos sean negativos
        aux_stack.push(i)

    while aux_stack.size() > 0:
        i = aux_stack.pop()
        instructions.push(i)


def follow_instruction(robot: Robot, instructions: Stack):
    aux_stack = Stack()
    while instructions.size() > 0:
        i = instructions.pop()
        aux_stack.push(i)
       
        robot.move(i[0],i[1])
    
    while aux_stack.size() > 0:
        i = aux_stack.pop()
        instructions.push(i)



robot1 = Robot()
print("Coordenadas Originales del Robot:")
print(robot1.location())
print("")

generate_instructions(instruction_historial)
print("Instrucciones: ")
instruction_historial.show() 
print("")


follow_instruction(robot1,instruction_historial)
print("Coordenadas del Robot tras seguir las Instrucciones:")
print(robot1.location())
print("")

backward_instructions(instruction_historial)
print("Instrucciones en Reversa: ")
instruction_historial.show() 
print("")

follow_instruction(robot1,instruction_historial)
print("Coordenadas del Robot tras seguir las Instrucciones:")
print(robot1.location())