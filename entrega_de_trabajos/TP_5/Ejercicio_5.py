from tree import BinaryTree

# a)
class Character:
    def __init__(self, name:str, is_villain: bool):
        self.__name = name
        self.__is_villain = is_villain

    def get_name(self):
        return self.__name
    def get_is_villain(self):
        return self.__is_villain

    def set_name(self, name:str):
         self.__name = name

capitanAmerica = Character("Capitan America", False)
thor = Character("Thor", False)
drStrange = Character("Dr Strange Tordo Raro", False)
doom = Character("Dr Doom", True)
ironMan = Character("Iron Man", False)
ciclope = Character("Ciclope", False)
thanos = Character("Thanos", True)

arbol_personajes = BinaryTree()

arbol_personajes.insert_node(capitanAmerica.get_name(), capitanAmerica)
arbol_personajes.insert_node(thor.get_name(), thor)
arbol_personajes.insert_node(drStrange.get_name(), drStrange)
arbol_personajes.insert_node(doom.get_name(), doom)
arbol_personajes.insert_node(ironMan.get_name(), ironMan)
arbol_personajes.insert_node(thanos.get_name(), thanos)
arbol_personajes.insert_node(ciclope.get_name(), ciclope)



# b)
def listar_villanos_alf(tree: BinaryTree[Character]):
        def __inorden(root):
            if root.left is not None:
                __inorden(root.left)
            if(root.other_values.get_is_villain()):
                print(root.value)
            if root.right is not None:
                __inorden(root.right)

        __inorden(tree.root)

# listar_villanos_alf(arbol_personajes)

# c)

def heroes_start_with(tree: BinaryTree[Character], initial_letter: str):
        def __inorden(root):
            if root.left is not None:
                __inorden(root.left)
            if (not (root.other_values.get_is_villain())) and ((root.value).lower()).startswith(initial_letter.lower()):
                print(root.value)
            if root.right is not None:
                __inorden(root.right)

        __inorden(tree.root)

# heroes_start_with(arbol_personajes, "c")

# d)

def heroe_count(tree: BinaryTree[Character]):
        def __count(root):
             if root is None:
                  return 0
             count = 0 if root.other_values.get_is_villain() else 1
             return count + __count(root.get_left()) + __count(root.get_right())

        return __count(tree.root)

# print(heroe_count(arbol_personajes))

# e)

def proxy_search(tree:BinaryTree, prefix: str):
        
    def __proxy_search(root, prefix):
        if root is None:
            return None
        
        found = __proxy_search(root.left, prefix)
        
        if found is not None:
             return found
        if prefix in root.value.lower():
             return root
        return __proxy_search(root.right, prefix)
        

    return __proxy_search(tree.root, prefix.lower())

def change_name(tree: BinaryTree, searched:str, new_name:str):
    character= proxy_search(tree, searched)
    if character is not None:
         old_value = character.value
         old_other_values = character.other_values
         old_other_values.set_name(new_name)
         tree.delete_node(old_value)
         tree.insert_node(new_name, old_other_values)
         print(f"se reemplazo {old_value} por {new_name}")
    else:
         print("No se encontro el personaje buscado")

# change_name(arbol_personajes, "strange", "Dr Strange")

# arbol_personajes.inorden()

# f)

def heroes_dec_order(tree:BinaryTree):
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            if not root.other_values.get_is_villain():
                print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(tree.root)

# heroes_dec_order(arbol_personajes)

#g)

arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def separateTree(original_tree: BinaryTree, heroes_tree: BinaryTree, villains_tree: BinaryTree):
    def __inorden(root):
                if root.left is not None:
                    __inorden(root.left)
                if (not (root.other_values.get_is_villain())):
                    heroes_tree.insert_node(root.value, root.other_values)
                else:
                    villains_tree.insert_node(root.value, root.other_values)
                if root.right is not None:
                    __inorden(root.right)
     
    __inorden(original_tree.root)

separateTree(arbol_personajes, arbol_heroes, arbol_villanos)

print("== Villanos ==")
print()
arbol_villanos.inorden()
print("== Heroes ==")
print()
arbol_heroes.inorden()

def count_nodes(tree: BinaryTree):

    def __count(root):
        if root is None:
             return 0
        return 1 + __count(root.left) + __count(root.right)

    return __count(tree.root)

print(f"Cantidad de villanos: {count_nodes(arbol_villanos)}")
print(f"Cantidad de heroes: {count_nodes(arbol_heroes)}")

arbol_heroes.inorden()
arbol_villanos.inorden()

