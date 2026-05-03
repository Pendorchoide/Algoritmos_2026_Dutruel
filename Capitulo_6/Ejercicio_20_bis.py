# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.-

from stack import Stack
from random import randint
from enum import Enum, auto

CARDINAL_POINTS = ["N","S","E","W","NE","SE","NW","SW"]
instruction_historial = Stack()

class CardinalPoints(Enum):
    N = auto()
    S = auto()
    E = auto()
    W = auto()
    NE = auto()
    SE = auto()
    NW = auto()
    SW = auto()


class Instruction:
    def __init__(self, direction: CardinalPoints, steps: int):
        self.__direction = direction
        self.__steps = steps
    
    def get_direction(self) -> CardinalPoints:
        return self.__direction
    
    def set_direction(self, direction: CardinalPoints):
        self.__direction = direction
    
    def get_steps(self) -> int:
        return self.__steps
    
    def negate_steps(self):
        self.__steps = -self.__steps
    
    def __str__(self):
        return f"[Direccion: {self.__direction}; Pasos: {self.__steps}]"


class Robot:
    
    def __init__(self):
        self.__x: float = 0
        self.__y: float = 0
    
    def move(self, instruction: Instruction):
        match instruction.get_direction():
            case CardinalPoints.N:
                self.__y += instruction.get_steps()
            case CardinalPoints.S:
                self.__y -= instruction.get_steps()
            case CardinalPoints.E:
                self.__x += instruction.get_steps()
            case CardinalPoints.W:
                self.__x -= instruction.get_steps()

            case CardinalPoints.NE:
                self.__y += instruction.get_steps() / 2
                self.__x += instruction.get_steps() / 2
            case CardinalPoints.SE:
                self.__y -= instruction.get_steps() / 2
                self.__x += instruction.get_steps() / 2
            case CardinalPoints.NW:
                self.__y += instruction.get_steps() / 2
                self.__x -= instruction.get_steps() / 2
            case CardinalPoints.SW:
                self.__y -= instruction.get_steps() / 2
                self.__x -= instruction.get_steps() / 2

    def location(self)-> tuple[float,float]:
        return (self.__x, self.__y)
    


def generate_instructions(instruction_container: Stack):
    for i in range(10):
        direction = list(CardinalPoints)[randint(0,7)]
        instruction = Instruction(direction, randint(1,5))
        instruction_historial.push(instruction)

def reverse_direction(direction: CardinalPoints) -> CardinalPoints:
    match direction:
        case CardinalPoints.N: return CardinalPoints.S
        case CardinalPoints.S: return CardinalPoints.N
        case CardinalPoints.E: return CardinalPoints.W 
        case CardinalPoints.W: return CardinalPoints.E
        case CardinalPoints.NE: return CardinalPoints.SW
        case CardinalPoints.SE: return CardinalPoints.NW
        case CardinalPoints.NW: return CardinalPoints.SE
        case CardinalPoints.SW: return CardinalPoints.NE


def backward_instructions(instructions: Stack):
    aux_stack = Stack()
    aux_stack2 = Stack()

    while instructions.size() > 0:
        i = instructions.pop()
        i.set_direction(reverse_direction(i.get_direction()))       #hace que la direccion sea la opuesta
        aux_stack.push(i)

    while aux_stack.size() > 0:
        i = aux_stack.pop()
        aux_stack2.push(i)

    while aux_stack2.size() > 0:
        i = aux_stack2.pop()
        instructions.push(i)


def follow_instruction(robot: Robot, instructions: Stack):
    aux_stack = Stack()
    while instructions.size() > 0:
        i = instructions.pop()
        aux_stack.push(i)
       
        robot.move(i)
    
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