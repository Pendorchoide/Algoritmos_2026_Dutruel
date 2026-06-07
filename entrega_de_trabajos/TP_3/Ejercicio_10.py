# 10. Dada una cola con las notifcaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notifcación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
#   a. escribir una función que elimine de la cola todas las notifcaciones de Facebook;
#   b. escribir una función que muestre todas las notifcaciones de Twiter, cuyo mensaje incluya
#   la palabra ‘Python’, si perder datos en la cola;
#   c. utilizar una pila para almacenar temporáneamente las notifcaciones producidas entre las
#   11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue
from stack import Stack
from random import randint

class Hour():
    def __init__(self, hh: int, mm: int, ss: int):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss
    
    def get_hh(self) -> int:
        return self.__hh

    def get_mm(self) -> int:
        return self.__mm
    
    def get_ss(self) -> int:
        return self.__ss

    def __str__(self) -> str:
        return f" {"0" * (2 - len( str(self.__hh)))}{self.__hh}:{"0" * (2 - len( str(self.__mm)))}{self.__mm}:{"0" * (2 - len( str(self.__ss)))}{self.__ss}"


class notification():

    def __init__(self, hour: Hour, app: str, msg: str):
        self.__hour = hour
        self.__app = app
        self.__msg = msg

    def get_hour(self) -> Hour:
        return self.__hour
    
    def get_app(self) -> str:
        return self.__app

    def get_msg(self) -> str:
        return self.__msg

    def __str__(self) -> str:
        return f"[{self.__app}, {self.__msg}, {self.__hour}]"


notifications_1 = Queue()
notifications_2 = Queue()
notifications_3 = Queue()

def random_notification() -> notification:
    APPS = ["Facebook", "Twitter", "Instagram", "YoutTube"]
    MSGS = ["I <3 Python!", "Tienes una nueva sugerencia de amistad", "¡Compra ya!", "Tienes un nuevo mensaje directo", "Aprende Python ya"]
    hour = Hour(randint(0,23), randint(0,59), randint(0,59))
    app = APPS[randint(0,3)]
    msg = MSGS[randint(0,4)]

    return notification(hour, app, msg)

def create_notifications(notifications: Queue):
    for i in range(10):
        notifications.arrive(random_notification())


create_notifications(notifications_1)
create_notifications(notifications_2)
create_notifications(notifications_3)

print ("Cola de notificaciones N°1")
notifications_1.show()
print("")

#print ("Cola de notificaciones N°2")
#notifications_2.show()
#print("")

#print ("Cola de notificaciones N°3")
#notifications_3.show()
#print("")


#   a. escribir una función que elimine de la cola todas las notifcaciones de Facebook;

def delete_facebook_nots(notifications: Queue):
    for i in range(notifications.size()):
        if notifications.on_front().get_app() == "Facebook":
            notifications.attention()
        else:
            notifications.move_to_end()

#   b. escribir una función que muestre todas las notifcaciones de Twiter, cuyo mensaje incluya
#   la palabra ‘Python’, sin perder datos en la cola;

def print_twitter_python(notifications: Queue):
    for i in range(notifications.size()):
        n = notifications.on_front()
        if (n.get_app() == "Twitter") and ("Python" in n.get_msg()):
            print(n)
        notifications.move_to_end()

#   c. utilizar una pila para almacenar temporáneamente las notifcaciones producidas entre las
#   11:43 y las 15:57, y determinar cuántas son.
def time_period_notif_counter(notifications: Queue)-> int:
    stack_aux = Stack()
    for i in range (notifications.size()):
        n_h = notifications.on_front().get_hour()
        if (n_h.get_hh() >= 11) and (n_h.get_hh() <= 15) and (n_h.get_mm() >= 43) and (n_h.get_mm() <= 57):
            stack_aux.push(notifications.on_front())
        notifications.move_to_end()
    return stack_aux.size()

#delete_facebook_nots(notifications_1)
print("Cola de notif. n°1 (sin Facebook)")
notifications_1.show()
print("")    

print("Twitter x Python")
print_twitter_python(notifications_1)
print("")    

print(f"Número de notificaciones entre 11:43 y 15:57: {time_period_notif_counter(notifications_1)}")