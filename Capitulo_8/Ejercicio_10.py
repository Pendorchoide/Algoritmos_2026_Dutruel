# 10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artis
# ta, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
# permita realizar las siguientes actividades:
#     a. obtener la información de la canción más larga;
#     b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
#     c. obtener todas las canciones de la banda Arctic Monkeys;
#     d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

from list_ import List

class Cancion:
    def __init__(self, nombre:str, autor:str, duracion_seg:int, reproducciones:int):
        self.__nombre = nombre
        self.__autor = autor
        self.__duracion_seg = duracion_seg
        self.__reproducciones = reproducciones

    def get_nombre(self):
        return self.__nombre

    def get_autor(self):
        return self.__autor

    def get_duracion_seg(self):
        return self.__duracion_seg

    def get_reproducciones(self):
        return self.__reproducciones

    def __str__(self):
        return f"{self.__nombre} - {self.__autor} - {self.__duracion_seg}s - {self.__reproducciones} reproducciones"


lista_canciones = List()

lista_canciones.insert_value(0, Cancion("Do I Wanna Know?", "Arctic Monkeys", 272, 5))
lista_canciones.insert_value(1, Cancion("Shape of You", "Ed Sheeran", 233, 4))
lista_canciones.insert_value(2, Cancion("Blinding Lights", "The Weeknd", 200, 1))
lista_canciones.insert_value(3, Cancion("Yesterday", "The Beatles", 125, 9))
lista_canciones.insert_value(4, Cancion("Stay", "The Kid LAROI", 141, 10))
lista_canciones.insert_value(5, Cancion("Fluorescent Adolescent", "Arctic Monkeys", 182, 2))
lista_canciones.insert_value(6, Cancion("Levitating", "Dua Lipa", 203, 3))
lista_canciones.insert_value(7, Cancion("Bohemian Rhapsody", "Queen", 355, 7))
lista_canciones.insert_value(8, Cancion("Watermelon Sugar", "Harry Styles", 174, 8))
lista_canciones.insert_value(9, Cancion("505", "Arctic Monkeys", 253, 6))

def por_reproducciones(item: Cancion):
    return item.get_reproducciones()

def por_duracion_seg(item: Cancion):
    return item.get_duracion_seg()

def por_nombre(item: Cancion):
    return item.get_nombre()

def por_autor(item: Cancion):
    return item.get_autor()

lista_canciones.add_criterion("reproducciones", por_reproducciones)
lista_canciones.add_criterion("duracion_seg", por_duracion_seg)
lista_canciones.add_criterion("nombre", por_nombre)
lista_canciones.add_criterion("autor", por_autor)


def cancion_mas_larga(canciones: List)-> Cancion:
    canciones.sort_by_criterion("duracion_seg")
    return canciones[-1]


def top_5(canciones: List)->List:
    canciones.sort_by_criterion("reproducciones")
    canciones.reverse()
    top_5_list = List()
    for i in range (5):
        top_5_list.append(canciones[i])
    return top_5_list

def arctic_monkeys(canciones:List)->List:
    arctic_monkeys_list = List()
    canciones.sort_by_criterion("autor")
    for i in range(canciones.size()):
        if canciones[i].get_autor() == "Arctic Monkeys":
            arctic_monkeys_list.append(canciones[i])
    return arctic_monkeys_list

def solo_una_palabra(canciones: List)->List:
    for i in range(canciones.size()):
        if " " not in canciones[i].get_nombre():
            print(canciones[i].get_nombre())

print("Cancion mas larga")
print(cancion_mas_larga(lista_canciones))

print("")
print("Top 5")
top_5(lista_canciones).show()

print("")
print("Arctic Monkeys Songs")
arctic_monkeys(lista_canciones).show()

print("")
print("Bandas con solo una palabra")
solo_una_palabra(lista_canciones)
