from tree import BinaryTree
from random import randint

arbol = BinaryTree()

for i in range(1
+0):
    arbol.insert_node(randint(1,10))

# A)
def count_nodes(tree: BinaryTree):
    def __count(root):
        if root is not None:
            return 1 + __count(root.left) + __count(root.right)
        else:
            return 0
        
    return __count(tree.root) 

# B)

def count_leaves(tree: BinaryTree):
    def __count(root):
        count = 0
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            return 1
        if root.left is not None:
            count += __count(root.left)
        if root.right is not None:
            count += __count(root.right)
        return count
        
    return __count(tree.root) 

arbol.by_level()

print(f"hojas{count_leaves(arbol)}")

# C)

def show_leaves(tree:BinaryTree):
    def __count(root):
            count = 0
            if root is None:
                return 0
            if (root.left is None) and (root.right is None):
                print(root)
            if root.left is not None:
                __count(root.left)
            if root.right is not None:
                __count(root.right)
            return count
            
    __count(tree.root) 

print("Hojas:")
show_leaves(arbol)

# D)

def father_of_searched(tree: BinaryTree, searched):
    def __search(root, value, father):
                aux = None
                if root is not None:
    
                    if root.value == value:
                        return father
                    elif value < root.value:
                        return __search(root.left, value, root)
                    elif value > root.value:
                        return __search(root.right, value, root)
    
                return aux
    
    return __search(tree.root, searched, None)
    
print("Father of 7")
print(father_of_searched(arbol, 7))

# E)

def tree_height(tree:BinaryTree):
    def __height(root):
        if root is None:
            return 0
        else:
            height_l = 1
            height_r = 1
            if root.left is not None:
                height_l += __height(root.left)
            if root.right is not None:
                height_r += __height(root.right)
            if (root.left is None) and (root.right is None):
                return 1
            else:
                return height_l if height_l > height_r else height_r
        
                
    height = __height(tree.root) - 1
    return (height) if height > 0 else None

print(f"Altura: {tree_height(arbol)}")
