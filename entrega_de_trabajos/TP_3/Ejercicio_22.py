# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro
# manoﬀ, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scot Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

from queue_ import Queue


class Character():

    def __init__(self, civil_name: str, hero_name: str, gender: str):
        self.__civil_name = civil_name
        self.__hero_name = hero_name
        self.__gender = gender
    
    def get_civil_name(self) -> str:
        return self.__civil_name
    
    def get_hero_name(self) -> str:
        return self.__hero_name

    def get_gender(self) -> str:
        return self.__gender
    
    def __str__(self) -> str:
        return f"[civil name: {self.__civil_name}, hero name: {self.__hero_name}, gender: {self.__gender}]"

marvel_characters = Queue()

marvel_characters.arrive(Character("Tony Stark", "Iron Man", "M"))
marvel_characters.arrive(Character("Steve Rogers", "Capitán América", "M"))
marvel_characters.arrive(Character("Natasha Romanoﬀ", "Black Widow", "F"))
marvel_characters.arrive(Character("Carol Danvers", "Capitana Marvel", "F"))
marvel_characters.arrive(Character("Scot Lang", "Ant Man", "M"))
marvel_characters.arrive(Character("Peter Parker", "Spider Man", "M"))


# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

def find_CM_civil_name(characters: Queue) -> str:
    for i in range(characters.size()):
        if characters.on_front().get_hero_name() == "Capitana Marvel":
            return characters.on_front().get_civil_name()
        characters.move_to_end()
    

# b. mostrar los nombres de los superhéroes femeninos;

def list_female_heroines(characters: Queue):
    for i in range(characters.size()):
        if characters.on_front().get_gender() == "F":
            print(characters.on_front().get_hero_name())
        characters.move_to_end()


# c. mostrar los nombres de los personajes masculinos;

def list_male_characters(characters: Queue):
    for i in range(characters.size()):
        if characters.on_front().get_gender() == "M":
            print(characters.on_front().get_civil_name())
        characters.move_to_end()


# d. determinar el nombre del superhéroe del personaje Scot Lang;

def find_Scot_Lang_hero_name(characters: Queue) -> str:
    for i in range(characters.size()):
        if characters.on_front().get_civil_name() == "Scot Lang":
            return characters.on_front().get_hero_name()
        characters.move_to_end()
        
        
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;

def list_s_name_characters(characters: Queue):
    for i in range(characters.size()):
        character = characters.on_front()
        if character.get_civil_name()[0] == "S" or character.get_hero_name()[0] == "S":
            print(character)
        characters.move_to_end()


# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

def find_Carol_Danvers_hero_name(characters: Queue) -> str:
    for i in range(characters.size()):
        if characters.on_front().get_civil_name() == "Carol Danvers":
            return characters.on_front().get_hero_name()
        characters.move_to_end()
        
#a
captain_marvel_c_name = find_CM_civil_name(marvel_characters)
if captain_marvel_c_name:
    print(f"El nombre de civil de Capitana Marvel es {captain_marvel_c_name}")
else:
    print("Capitana Marvel no se Encuentra en la cola, no se pudo obtener su nombre de civil")

#b
print("")
print("= Heroinas Femeninas =")
list_female_heroines(marvel_characters)
print("")

#c
print("")
print("= Personajes Masculinos (nombre de civil) =")
list_male_characters(marvel_characters)
print("")

#d
scot_lang_h_name = find_Scot_Lang_hero_name(marvel_characters)
if scot_lang_h_name:
    print(f"El nombre de heroe de Scot Lang es {scot_lang_h_name}")
else:
    print("Scot Lang no se Encuentra en la cola, no se pudo obtener su nombre de heroe")

#e
print("")
print("= Personajes cuyo nombre (civil/hero) comienzan con S =")
list_s_name_characters(marvel_characters)
print("")

#f
carol_denvers_h_name = find_Carol_Danvers_hero_name(marvel_characters)
if carol_denvers_h_name:
    print(f"El nombre de heroina de Carol Denvers es {carol_denvers_h_name}")
else:
    print("Carol Denvers no se Encuentra en la cola, no se pudo obtener su nombre de civil")