# 23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto defnido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

lab = [
    [1,0,0,0,0],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1],
    [0,1,1,1,1]
]

def lab_solver(laberynth: list[list], index_x = 0, index_y = 0):
    print("==========")
    print(laberynth[0])
    print(laberynth[1])
    print(laberynth[2])
    print(laberynth[3])
    print(laberynth[4])
    print("==========")
    laberynth[index_y][index_x] = 2


    if (index_x == len(laberynth) - 1) and (index_y == len(laberynth) - 1):
        return ("se llego <3")

    if index_x < len(laberynth) - 1:
        if laberynth[index_y][index_x + 1] == 1:
            new_index_x = index_x + 1 
            response = lab_solver(laberynth, new_index_x, index_y)
            if response != "volve":
                return response

        
    if index_y < len(laberynth) - 1:
        if laberynth[index_y + 1][index_x] == 1:
            new_index_y = index_y + 1 
            response = lab_solver(laberynth, index_x, new_index_y)
            if response != "volve":
                return response
    
    if index_x > 0:
        if laberynth[index_y][index_x - 1] == 1:
            new_index_x = index_x - 1 
            response = lab_solver(laberynth, new_index_x, index_y)
            if response != "volve":
                return response


    if index_y > 0:
        if laberynth[index_y - 1][index_x] == 1:
            new_index_y = index_y - 1 
            return lab_solver(laberynth, index_x, new_index_y)
        
    return "volve"
        
lab_response = lab_solver(lab)
if lab_response == "volve":
    print("No es posible resolver el laberinto")
else:
    print(lab_response)
    


