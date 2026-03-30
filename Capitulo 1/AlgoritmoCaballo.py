import os

phoneBoard = [
    [-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1],
    [-1,-1, 7, 8, 9,-1,-1],
    [-1,-1, 4, 5, 6,-1,-1],
    [-1,-1, 1, 2, 3,-1,-1],
    [-1,-1,-1, 0,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1],
]

def FindInitialNumberCoord(board:list[list],Num:int) -> tuple:
    initialPosY = int
    initialPosX = int
    for i in range(len(board)):
        if Num in board[i]:
            initialPosY = i            
            initialPosX = board[i].index(Num)
    return (initialPosX,initialPosY)


def GetChildren(board:list[list],father:int)->list:
    children = list()
    
    x = FindInitialNumberCoord(board,father)[0]
    y = FindInitialNumberCoord(board,father)[1]


    if (board[y-2][x-1] != -1):
            children.append(board[y-2][x-1])
    if (board[y-2][x+1] != -1):
            children.append(board[y-2][x+1])

    if (board[y+2][x-1] != -1):
            children.append(board[y+2][x-1])
    if (board[y+2][x+1] != -1):
            children.append(board[y+2][x+1])

    if (board[y-1][x-2] != -1):
            children.append(board[y-1][x-2])
    if (board[y+1][x-2] != -1):
            children.append(board[y+1][x-2])
    
    if (board[y-1][x+2] != -1):
            children.append(board[y-1][x+2])
    if (board[y+1][x+2] != -1):
            children.append(board[y+1][x+2])
    
    return children


def GetChildrenList(board: list[list],fathers:list):
    auxFathers = fathers
    children = list()
    for father in auxFathers:
        for elem in GetChildren(board,father):
            children.append(elem)
    return children

def CountMovesFromList(board:list[list],num):
    counter = int(0)
    x = FindInitialNumberCoord(board,num)[0]
    y = FindInitialNumberCoord(board,num)[1]

    if (board[y-2][x-1] != -1):
        counter += 1
    if (board[y-2][x+1] != -1):
        counter += 1

    if (board[y+2][x-1] != -1):
        counter += 1
    if (board[y+2][x+1] != -1):
        counter += 1

    if (board[y-1][x-2] != -1):
        counter += 1
    if (board[y+1][x-2] != -1):
        counter += 1
    
    if (board[y-1][x+2] != -1):
        counter += 1
    if (board[y+1][x+2] != -1):
        counter += 1
    
    return counter

def CalculateAllPossibleMoves(board:list[list],initPos:int,numOfMoves:int)->int:
    fathers = [initPos]
    for move in range(numOfMoves - 1):
        fathers = GetChildrenList(board,fathers)

    counter = int(0)
    for elem in fathers:
        counter += CountMovesFromList(board,elem)

    return counter


########## Main ##########

finalCounter = int(0)

numOfMoves = int(input("Ingrese cuantos movimientos puede hacer el caballo: "))

if numOfMoves > 0:
     
    print("")

    for initPos in range(10):
        finalCounter += CalculateAllPossibleMoves(phoneBoard,initPos,numOfMoves)

    print("Con ",numOfMoves," moviemientos, existen ",finalCounter," posibilidades!")
else:
    print("PorFavor ingrese un número de movimientos entero positivo")