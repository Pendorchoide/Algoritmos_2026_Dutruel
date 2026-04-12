#5. Desarrollar una función que permita convertir un número romano en un número decimal

def roman_char_to_int(letter: str)->int:
        match letter:
            case "I":
                return 1
            case "V":
                return 5
            case "X":
                return 10
            case "L":
                return 50
            case "C":
                return 100
            case "D":
                return 500
            case "M":
                return 1000
            case _:
                print("Se ingreso un caracter no valido")
                return -1

def roman_to_dec(roman:str, i:int = 0)->int:
    """Convierte un número romano a decimal.
    Args:
        roman (str): El número romano a convertir.
        i (int, opcional): El índice actual en el string. Por defecto 0.
    Returns:
        int: El número decimal equivalente al número romano.
    """

    if i >= len(roman):         # Condición de pare (cuando el str termina)
        return 0
    
    current_num = roman_char_to_int(roman[i])
    
    if current_num == -1:       # En caso de que se haya ingresado un caracter no valido
        return 0

    if i + 1 < len(roman):
        next_num = roman_char_to_int(roman[i+1])
        
        if next_num > current_num:
            return (next_num - current_num) + roman_to_dec(roman, i + 2)
        else:
            return current_num + roman_to_dec(roman, i + 1)


    
    
    

roman_num = input("Ingrese un número romano (todo en mayúsc): ")
print("El numero ",roman_num," se expresa como ",roman_to_dec(roman_num)," en decimal.")