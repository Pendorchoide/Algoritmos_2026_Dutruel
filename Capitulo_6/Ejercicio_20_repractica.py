# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.-

from stack import Stack
from random import randint
from enum import Enum


directions = ["N","E","NE","NW","SE","SW","W","S"]

class Movimiento:
    def __init__(self, pasos:int, direccion:str):
        self.__pasos = pasos
        self.__direccion = direccion

    def get_pasos(self)->int:
        return self.__pasos
    
    def get_direccion(self)->str:
        return self.__direccion
    
    def reverse(self):
        self.__direccion = directions[7-directions.index(self.__direccion)]
    
    def __str__(self):
        return f"[pasos: {self.__pasos}, direccion: {self.__direccion}]"
    

class Robot:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def move(self, movimiento: Movimiento):
        if "N" == movimiento.get_direccion():
            self.__y += 1 * movimiento.get_pasos()
        elif "S" == movimiento.get_direccion():
            self.__y -= 1 * movimiento.get_pasos()
        elif "E" == movimiento.get_direccion():
            self.__x += 1 * movimiento.get_pasos()
        elif "O" == movimiento.get_direccion():
            self.__x -= 1 * movimiento.get_pasos()

        elif "NE" == movimiento.get_direccion():
            self.__x += 0.5 * movimiento.get_pasos()
            self.__y += 0.5 * movimiento.get_pasos()
        elif "NW" == movimiento.get_direccion():
            self.__x -= 0.5 * movimiento.get_pasos()
            self.__y += 0.5 * movimiento.get_pasos()
        elif "SE" == movimiento.get_direccion():
            self.__x += 0.5 * movimiento.get_pasos()
            self.__y -= 0.5 * movimiento.get_pasos()
        elif "SW" == movimiento.get_direccion():
            self.__x -= 0.5 * movimiento.get_pasos()
            self.__y -= 0.5 * movimiento.get_pasos()
            

    def __str__(self):
        return f"[x: {self.__x}, y: {self.__y}]"


def rand_move():
    return Movimiento(randint(1,3),directions[randint(0,7)])


def mover_robot(robot: Robot, movimiento: Movimiento, historial: Stack):
    robot.move(movimiento)
    historial.push(movimiento)

def mover_robot_reversa(robot:Robot, historial: Stack):
    aux_stack = Stack()
    for _ in range(historial.size()):
        movimiento = historial.pop()
        movimiento.reverse()
        robot.move(movimiento)
        aux_stack.push(movimiento)
    while aux_stack.size() > 0:
        historial.push(aux_stack.pop())

roboto = Robot()

historial_movimientos = Stack()


print("= Robot desde 0 =")
print(roboto)

for _ in range(5):
    mover_robot(roboto, rand_move(), historial_movimientos)

print("= Robot tras 10 movimientos =")
print(roboto)

print("")
print("= El Historial =")
historial_movimientos.show()

mover_robot_reversa(roboto, historial_movimientos)

print("")
print("= Robot de vuelta =")
print(roboto)

print("")
print("= El Historial =")
historial_movimientos.show()