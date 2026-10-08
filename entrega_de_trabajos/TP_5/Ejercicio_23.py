from tree import BinaryTree

class Creature:
    def __init__(self, name, defeated_by = None, description: str = None, captured_by: str = None, partially_defeated_by:str = None):
        self.__name = name
        self.__defeated_by = defeated_by
        self.__description = description
        self.__captured_by = captured_by
        self.__partially_defeated_by = partially_defeated_by

    def get_name(self):
        return self.__name

    def get_defeated_by(self):
        return self.__defeated_by

    def get_captured_by(self):
            return self.__captured_by

    def get_description(self):
        return self.__description

    def set_name(self, name):
        self.__name = name
        
    def set_description(self, description):
        self.__description = description

    def set_captured_by(self, catcher):
        self.__captured_by = catcher

    def set_partially_defeated_by(self, partially_defeated_by):
            self.__partially_defeated_by = partially_defeated_by

    def __str__(self):
        result = f"____________________.____________________\nCreature: {self.__name}"
        if self.__defeated_by is not None:
            result += f"\nDefeated by: {self.__defeated_by}"
        if self.__description is not None:
            result += f"\nDescription: {self.__description}"
        if self.__captured_by is not None:
                    result += f"\nCatcher: {self.__captured_by}"
        if self.__partially_defeated_by is not None:
                            result += f"\nPartially defeated by: {self.__partially_defeated_by}"
        result += ("\n____________________.____________________\n")
        return result


arbol_criaturas = BinaryTree()

arbol_criaturas.insert_node("Ceto", Creature("Ceto"))
arbol_criaturas.insert_node("Tifon", Creature("Tifon", "Zeus"))
arbol_criaturas.insert_node("Equidna", Creature("Equidna", "Argos Panoptes"))
arbol_criaturas.insert_node("Dino", Creature("Dino"))
arbol_criaturas.insert_node("Pefredo", Creature("Pefredo"))
arbol_criaturas.insert_node("Enio", Creature("Enio"))
arbol_criaturas.insert_node("Escila", Creature("Escila"))
arbol_criaturas.insert_node("Caribdis", Creature("Caribdis"))
arbol_criaturas.insert_node("Euriale", Creature("Euriale"))
arbol_criaturas.insert_node("Esteno", Creature("Esteno"))
arbol_criaturas.insert_node("Medusa", Creature("Medusa", "Perseo"))
arbol_criaturas.insert_node("Ladon", Creature("Ladon", "Heracles"))
arbol_criaturas.insert_node("Aguila" , Creature("Aguila del Caucaso"))
arbol_criaturas.insert_node("Quimera", Creature("Quimera", "Belerofonte"))
arbol_criaturas.insert_node("Hidra" , Creature("Hidra de Lerna", "Heracles"))
arbol_criaturas.insert_node("Leon" , Creature("Leon de Nemea", "Heracles"))
arbol_criaturas.insert_node("Esfinge", Creature("Esfinge", "Edipo"))
arbol_criaturas.insert_node("Dragon" , Creature("Dragon  de la Coloquida"))
arbol_criaturas.insert_node("Cerbero", Creature("Cerbero"))

arbol_criaturas.insert_node("Cerda de Cromion", Creature("Cerda de Cromion", "Teseo"))
arbol_criaturas.insert_node("Ortro", Creature("Ortro", "Heracles"))
arbol_criaturas.insert_node("Toro de Creta", Creature("Toro de Creta", "Teseo"))
arbol_criaturas.insert_node("Jabali de Calidon", Creature("Jabali de Calidon", "Atalanta"))
arbol_criaturas.insert_node("Carcinos", Creature("Carcinos"))
arbol_criaturas.insert_node("Gerion", Creature("Gerion", "Heracles"))
arbol_criaturas.insert_node("Cloto", Creature("Cloto"))
arbol_criaturas.insert_node("Laquesis", Creature("Laquesis"))
arbol_criaturas.insert_node("Atropos", Creature("Atropos"))
arbol_criaturas.insert_node("Minotauro de Creta", Creature("Minotauro de Creta", "Teseo"))
arbol_criaturas.insert_node("Harpias", Creature("Harpias"))
arbol_criaturas.insert_node("Argos Panoptes", Creature("Argos Panoptes", "Hermes"))
arbol_criaturas.insert_node("Aves del Estinfalo", Creature("Aves del Estinfalo"))
arbol_criaturas.insert_node("Talos", Creature("Talos", "Medea"))
arbol_criaturas.insert_node("Sirenas", Creature("Sirenas"))
arbol_criaturas.insert_node("Piton", Creature("Piton", "Apolo"))
arbol_criaturas.insert_node("Cierva de Cerinea", Creature("Cierva de Cerinea"))
arbol_criaturas.insert_node("Basilisco", Creature("Basilisco"))
arbol_criaturas.insert_node("Jabali de Erimanto", Creature("Jabali de Erimanto"))
# A)

def list_creatures(tree: BinaryTree):
    def __list(root):
        if root is not None:
            if root.left is not None:
                __list(root.left)
            print(root.other_values)
            if root.right is not None:
                __list(root.right)
        
    __list(tree.root)


# list_creatures(arbol_criaturas)

# B)

def add_description(tree: BinaryTree, creature: str, description: str):
    finded =tree.search(creature)
    if (finded is not None):
        finded.other_values.set_description(description)
    else:
        print("criatura no encontrada")

add_description(arbol_criaturas, "Medusa", "Capaz de petrificar con la mirada")

# list_creatures(arbol_criaturas)

# C)

def print_creature(tree: BinaryTree, creature: str):
    finded = tree.search(creature)
    if (finded) is not None:
        print(finded.other_values)
    else:
        print("criatura no encontrada")

# print_creature(arbol_criaturas, "Medusa")
# print_creature(arbol_criaturas, "Pefredo")

# D)

def top_n_heroes(tree: BinaryTree, positions:int):
    all_heroes = {}

    def __inorden(root):
        if root is not None:
            if root.left is not None:
                __inorden(root.left)

            hero = root.other_values.get_defeated_by()
            if hero is not None:
                if hero in all_heroes:
                    all_heroes[hero] += 1
                else:
                    all_heroes[hero] = 1
                
           
            if root.right is not None:
                __inorden(root.right)
            
    __inorden(tree.root)
    alph_sorted_heores = sorted(all_heroes.items(), key= lambda x: x[0]) # se rompe el desempate eligiendo al primero en orden alfabetico
    podium = dict(sorted(alph_sorted_heores, key= lambda x: x[1], reverse= True)[:positions])
    print(podium)

# top_n_heroes(arbol_criaturas,3)

# E)

def creatures_defeated_by(tree: BinaryTree, hero:str):
    def __inorden(root):
            if root is not None:
                if root.left is not None:
                    __inorden(root.left)

            if root.other_values.get_defeated_by() == hero:
                print(root)
           
            if root.right is not None:
                __inorden(root.right)
                        
    __inorden(tree.root)

# creatures_defeated_by(arbol_criaturas, "Heracles")

# F)

def list_undefeated_creatures(tree: BinaryTree):
    def __inorden(root):
            if root is not None:
                if root.left is not None:
                    __inorden(root.left)

            if root.other_values.get_defeated_by() == None:
                print(root)
           
            if root.right is not None:
                __inorden(root.right)
                        
    __inorden(tree.root)

# creatures_defeated_by(arbol_criaturas, "Heracles")

# list_undefeated_creatures(arbol_criaturas)

# G)

def add_catcher(tree: BinaryTree, creature: str, catcher: str):
    finded = tree.search(creature)
    if (finded) is not None:
        finded.other_values.set_captured_by(catcher)
    else:
        print("criatura no encontrada")

# H)

add_catcher(arbol_criaturas, "Cerbero", "Heracles")
add_catcher(arbol_criaturas, "Toro de Creta", "Heracles")
add_catcher(arbol_criaturas, "Cierva de Cerinea", "Heracles")
add_catcher(arbol_criaturas, "Jabali de Erimanto", "Heracles")

# list_creatures(arbol_criaturas)

# I)

def proxy_search(tree:BinaryTree, content: str) -> None:
        
    def __proxy_search(root, content):
        if root is None:
            return None
        
        found = __proxy_search(root.left, content)
        
        if found is not None:
             return found
        if content in root.value.lower():
             return root
        return __proxy_search(root.right, content)
        
    return __proxy_search(tree.root, content.lower())

# print(proxy_search(arbol_criaturas, "med").other_values)

# J)
def delete_creature(tree: BinaryTree, creature: str):
    return tree.delete_node(creature)

delete_creature(arbol_criaturas, "Basilisco")
delete_creature(arbol_criaturas, "Sirenas")

# print_creature(arbol_criaturas, "Basilisco")
# print_creature(arbol_criaturas, "Sirenas")


# K)

def add_partially_defeated_by(tree: BinaryTree, creature: str, partially_defeated_by: str):
    finded = tree.search(creature)
    if (finded) is not None:
        finded.other_values.set_partially_defeated_by(partially_defeated_by)
    else:
        print("criatura no encontrada")

add_partially_defeated_by(arbol_criaturas, "Aves del Estinfalo", "Heracles")
# print_creature(arbol_criaturas, "Aves del Estinfalo")

# L)

def modify_creatures_name(tree: BinaryTree, creature: str, new_name: str):
    creature = proxy_search(tree, creature)
    
    if creature is not None:
        old_value = creature.value
        old_other_values = creature.other_values
        old_other_values.set_name(new_name)
        tree.delete_node(old_value)
        tree.insert_node(new_name, old_other_values)
        print(f"se reemplazo {old_value} por {new_name}")
    else:
        print("criatura no encontrada")

# modify_creatures_name(arbol_criaturas, "Ladon", "Dragon Ladon")

# print_creature(arbol_criaturas,"Dragon Ladon")

# M)

# arbol_criaturas.by_level()

# N)

def creatures_captured_by(tree: BinaryTree, catcher:str):
    def __inorden(root):
            if root is not None:
                if root.left is not None:
                    __inorden(root.left)

            if root.other_values.get_captured_by() == catcher:
                print(root)
           
            if root.right is not None:
                __inorden(root.right)
                        
    __inorden(tree.root)

creatures_captured_by(arbol_criaturas, "Heracles")