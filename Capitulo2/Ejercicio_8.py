# 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.

def ChainInvertion(chain:str)->str:

    if chain == "":
        return chain
    else:
        return chain[-1] + ChainInvertion(chain[:-1])

def DecimalToBinary(num:int)->int:
    if(num == 0) or (num == 1):
        return num
    else:
        chain = ""
        if num % 2 == 0:
            chain += "0"
        else:
            chain += "1"
    