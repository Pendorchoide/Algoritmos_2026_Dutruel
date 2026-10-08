from tree import BinaryTree
from random import randint

arbol = BinaryTree()

for i in range(15):
    arbol.insert_node(randint(1,30))

print("Arbol generado: ")
arbol.by_level()
print()

def get_minimun(tree: BinaryTree):
    def __get_minimun(root, min):
        if root.left is not None:
            if root.left.value <= min.value:
                return __get_minimun(root.left, root.left)
        return root
   
    if tree.root is not None:
        return __get_minimun(tree.root, tree.root)
    else: return None
    

def get_maximun(tree: BinaryTree):
    def __get_maximun(root, min):
        if root.right is not None:
            if root.right.value >= min.value:
                return __get_maximun(root.right, root.right)
        return root
   
    if tree.root is not None:
        return __get_maximun(tree.root, tree.root)
    else: return None

print(f"Maximo: {get_maximun(arbol)}")
print(f"Minimo: {get_minimun(arbol)}")
