#  Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:
#      a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
#      b. determinar si un número está cargado en el árbol o no;
#      c. eliminar tres valores del árbol;
#      d. determinar la altura del subárbol izquierdo y del subárbol derecho;
#      e. determinar la cantidad de ocurrencias de un elemento en el árbol;
#      f. contar cuántos números pares e impares hay en el árbol.

from random import randint
from tree import BinaryTree

arbol = BinaryTree()
arbol2= BinaryTree()

def cargar_1000_numeros(arbol: BinaryTree):
    for i in range(0,10):
        arbol.insert_node(randint(1, 10000))

cargar_1000_numeros(arbol)

# a)
print("========= inorden ========")
arbol.inorden()
# print("========= postorden ========")
# arbol.postorden()
# print("========= preorden ========")
# arbol.preorden()
# print("========= by_level ========")
# arbol.by_level()

# b)
# def isInTree(arbol:BinaryTree, num: int)->bool:
#     founded = arbol.search(num)
#     return founded
# print()
# if isInTree(arbol, int(input("Ingrese el numero que desea buscar: "))):
#     print("El numero se encuentra en el arbo!")
# else:
#     print("El numero NO se encuentra en el arbo!")

# # c)
# print("==============")
# for i in range(3):
#     node , aux = arbol.delete_node(int(input("ingrese un valor para eliminar: ")))
#     if (node is not None):
#         print("Eliminado correctamente!")
#     else:
#         print("Ese numero no pertenece al arbol!")

# print("========= inorden ========")
# arbol.inorden()

# d)
print("==============")

def alturaRamaIzquierda(arbol: BinaryTree)->int:

    def __alturaRamaIzquierda(node):

        if (node is not None):
            porIz = 0
            porDer = 0
            if (node.left is not None):
                porIz = 1 + __alturaRamaIzquierda(node.left)
            if (node.right is not None):
                porDer = 1 + __alturaRamaIzquierda(node.right)

            if porIz > porDer:
                return porIz
            else:
                return porDer
    count = __alturaRamaIzquierda(arbol.root.left)
    return count

def alturaRamaDerecha(arbol: BinaryTree)->int:

    def __alturaRamaDerecha(node):

        if (node is not None):
            porIz = 0
            porDer = 0
            if (node.left is not None):
                porIz = 1 + __alturaRamaDerecha(node.left)
            if (node.right is not None):
                porDer = 1 + __alturaRamaDerecha(node.right)

            if porIz > porDer:
                return porIz
            else:
                return porDer
    count = __alturaRamaDerecha(arbol.root.right)
    return count

print(f"Altura de la rama izquierda: {alturaRamaIzquierda(arbol)}")
print(f"Altura de la rama derecha: {alturaRamaDerecha(arbol)}")

# e) Determinar Ocurrencias

# def determinar_ocurrencias(arbol: BinaryTree, valor: int) -> int:
#     def contar(node):
#         if node is None:
#             return 0

#         total = 1 if node.value == valor else 0
#         total += contar(node.left)
#         total += contar(node.right)
#         return total

#     return contar(arbol.root) if arbol.root is not None else 0

# arbol.insert_node(23)
# arbol.insert_node(23)
# arbol.insert_node(23)

# print(f"Ocurrencias: {determinar_ocurrencias(arbol, 23)}")

# f) Contar números pares e impares

def pares(arbol: BinaryTree,) -> int:
    def contar(node):
        if node is None:
            return 0

        total = 1 if ((node.value % 2) == 0) else 0
        total += contar(node.left)
        total += contar(node.right)
        return total

    return contar(arbol.root) if arbol.root is not None else 0

def impares(arbol: BinaryTree,) -> int:
    def contar(node):
        if node is None:
            return 0

        total = 1 if ((node.value % 2) != 0) else 0
        total += contar(node.left)
        total += contar(node.right)
        return total

    return contar(arbol.root) if arbol.root is not None else 0

print(f"Pares {pares(arbol)}")
print(f"Impares {impares(arbol)}")

arbol2.insert_node(5)
arbol2.insert_node(4)
arbol2.insert_node(6)
arbol2.insert_node(3)
arbol2.insert_node(5)
arbol2.insert_node(7)

arbol2.by_level()

