#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida

def Invertion(l:list)->list:



    if len(l) == 1:
        return l
    elif len(l) == 2:
        aux = l[0]
        l[0] = l[1]
        l[1] = aux
        return l
    else:
        first = l[0]
        last = l[len(l)-1]
        l.pop(0)
        l.pop()
        l= Invertion(l)
        l.insert(0,last)
        l.append(first)
        return l

chain = input("Ingrese una cadena de caracteres para invertir: ")

print("Lista Invertida:","".join(Invertion(list(chain))))