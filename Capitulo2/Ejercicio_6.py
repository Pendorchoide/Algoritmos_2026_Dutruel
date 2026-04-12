#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida

def ChainInvertion(chain:str)->str:

    if chain == "":
        return chain
    else:
        return chain[-1] + ChainInvertion(chain[:-1])

chain = input("Ingrese una cadena de caracteres para invertir: ")

print("Lista Invertida:","".join(ChainInvertion(chain)))