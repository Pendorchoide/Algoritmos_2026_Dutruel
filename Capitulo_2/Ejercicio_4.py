#4. Implementar una función para calcular la potencia 
# dado dos números enteros, el primero representa la base y segundo el exponente

def ExpInt(base:int,exp:int)->int:
    if exp == 0:
        return 1
    elif base == 0 or base == 1:
        return base
    else:
        return base * ExpInt(base,exp-1)
    

val1 = int(input("Ingrese una base: "))
val2 = int(input("Ingrese un exponente: "))
print('El resultado de ',val1," elevado a ",val2," es: ", ExpInt(val1,val2))