#5. Desarrollar una función que permita convertir un número romano en un número decimal

def RomanStrToIntList(roman:str)->list[int]:
    listInt = list(roman)
    i = 0
    for letter in listInt:
        match letter:
            case "I":
                listInt[i] = 1
            case "V":
                listInt[i] = 5
            case "X":
                listInt[i] = 10
            case "L":
                listInt[i] = 50
            case "C":
                listInt[i] = 100
            case "D":
                listInt[i] = 500
            case "M":
                listInt[i] = 1000
            case _:
                print("Se ingreso un caracter no valido")
                return 0
        i+=1
    return listInt

def RomanCal(lista:list)->int:
    if len(lista) == 1:
        return lista[0]

    elif lista[0] < lista[1]:
        first = lista[0]
        aux = lista
        aux.pop(0)
        return RomanCal(aux) - first
    else:
        first = lista[0]
        aux = lista
        aux.pop(0)
        return RomanCal(aux) + first

def RomanToDec(roman:str)->int:
    listInt = RomanStrToIntList(roman)
    return RomanCal(listInt)
    
    

romanNum = input("Ingrese un número romano (todo en mayúsc): ")
print("El numero ",romanNum," se expresa como ",RomanToDec(romanNum)," en decimal.")