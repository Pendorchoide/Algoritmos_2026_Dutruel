from tree import BinaryTree, Node
from typing import Any

# Implementar un algoritmo que contemple dos funciones, la
# primera que devuelva el hijo derecho de un nodo y la segunda que devuelva el hijo 
# izquierdo.

def return_left_son(tree: BinaryTree, node: Any):
    return tree.search(node).get_left()

def return_right_son(tree: BinaryTree, node: Any):
    return tree.search(node).get_right()
    

arbol = BinaryTree()

arbol.insert_node(2)
arbol.insert_node(24)
arbol.insert_node(4)
arbol.insert_node(52)
arbol.insert_node(2)


print(f"Hijo izq de 52:{return_left_son(arbol, 52)}")
print(f"Hijo der de 52:{return_right_son(arbol, 52)}")
print(f"Hijo izq de 4:{return_left_son(arbol, 4)}")
print(f"Hijo der de 4:{return_right_son(arbol, 4)}")
print(f"Hijo izq de 2:{return_left_son(arbol, 2)}")
print(f"Hijo der de 2:{return_right_son(arbol, 2)}")
print(f"Hijo izq de 24:{return_left_son(arbol, 24)}")
print(f"Hijo der de 24:{return_right_son(arbol, 24)}")

arbol.by_level()