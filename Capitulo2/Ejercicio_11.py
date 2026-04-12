#  11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena

def CountDigits(num:int)->int:
    if (num // 10) == 0:
        return 1
    else:
        return CountDigits(num // 10) + 1

def InvertInt(num:int)->int:
    if num < 10:            # ej:  1 -> 1
        return num
    elif (num < 100):        ## ej:  23  | first = 2 | last = (23 % 10) = 3 | -> 30 + 2 = 32
        first = num // 10
        last = num % 10
        return (last*10) + first
    else:
        digits = CountDigits(num)              #           | digits = 5 
        first = num // (10**(digits-1))        #ej: 12345  | first = 12345 // 10**4 = 1
        last = num % 10                        #           | last = 12345 % 10 = 5
        middleNums = ((num // 10) % (10**(digits-2)))    # middleNums = (12345//10) % (10 ** 3) = 1234 % 1000 = 234
        return ((last * (10**(digits-1)) + (InvertInt(middleNums)) * 10) + first)  # return = 5 * (10**4) + (432 * 10) + 1 = 50000 + 4320 + 1 = 54321

print("El número invertido es: ",InvertInt(int(input("Ingrese un número para invertir: "))))
