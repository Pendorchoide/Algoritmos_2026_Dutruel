from tree import BinaryTree
from random import randint
from queue_ import Queue

arbol = BinaryTree()

for i in range(15):
    arbol.insert_node(randint(1,1000))

print("Arbol generado: ")
arbol.by_level()
print()

def count_nodes_in_level(tree: BinaryTree, level:int) -> None:
    pendings = Queue()

    if tree.root is not None:
        pendings.arrive(tree.root)

        lvl = 0
        while(pendings.size()>0):
            if lvl == level:
                return (pendings.size())

            for i in range(pendings.size()):
                node = pendings.attention()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
            lvl += 1

def is_level_complete(tree: BinaryTree, level:int):
    n = count_nodes_in_level(tree, level)
    if n is not None:
        if (2**level) > n:
            return (2**level) - n
        return 0
    else:
        return 2**level

print("=============================")
lvl_selected = 3
nodos = count_nodes_in_level(arbol, lvl_selected)
if (nodos is not None):
    print(f"nodos en el nivel {lvl_selected}: {nodos}")
completitude = is_level_complete(arbol,lvl_selected)
if (completitude == 0):
    print(f"El nivel {lvl_selected} esta completo")
else:
    print(f"El nivel {lvl_selected} esta incompleto, le faltan {completitude} nodos")
