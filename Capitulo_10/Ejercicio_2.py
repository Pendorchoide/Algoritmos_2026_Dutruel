from tree_not_balanced import U_BinaryTree

arbol = U_BinaryTree()


def load_expression(u_tree: U_BinaryTree,expression:str):
    for c in expression:
        if c != " ":
            u_tree.insert_node(c)

load_expression(arbol, "(2 + 3) * (2 * 5)")

print("By level:")
arbol.by_level()
print("Inorden")
arbol.inorden()
print("Postorden")
arbol.postorden()
print("Preorden")
arbol.preorden()