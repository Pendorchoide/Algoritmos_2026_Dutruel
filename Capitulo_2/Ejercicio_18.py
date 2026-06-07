#Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.

matx = [[1,2,3],
       [4,5,6],
       [7,8,9]]

def mostrar_matriz(mat: list[list]):
    n = len(mat)
    if n > 0:
        m = len(mat[0])

    if n == 0:
        return
    elif m == 0:
        mat.pop(0)
        print("")
        return mostrar_matriz(mat)
    else:
        print(mat[0].pop(0),end="")
        return mostrar_matriz(mat)
    

mostrar_matriz(matx)