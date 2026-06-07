# 12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fet están en dicha pila sin perder los datos.

from stack import Stack

star_wars = Stack()
star_wars_2 = Stack()


star_wars.push("Yoda")
star_wars.push("Luke Skywalker")
star_wars.push("Leia Organa")
star_wars.push("Rey")
star_wars.push("Boba Fet")
star_wars.push("Darth Vader")



star_wars.push("Yoda")
star_wars.push("Luke Skywalker")
star_wars.push("Rey")
star_wars.push("Darth Vader")

def encontrar_leia_boba(p: Stack)->bool:
    p_aux = Stack()
    founded = False
    while p.size() > 0:
        character = p.pop()
        if character == "Leia Organa" or character == "Boba Fet":
            founded = True
        p_aux.push(character)
    
    while p_aux.size()>0:
        p.push(p_aux.pop())

    return founded

print(encontrar_leia_boba(star_wars))
print(encontrar_leia_boba(star_wars_2))
