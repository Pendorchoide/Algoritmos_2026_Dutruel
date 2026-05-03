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

def roman_to_dec(roman:str, i:int = 0, repeat_counter: int = 0)->int:
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
        return -1

    if i + 1 < len(roman):
        next_num = roman_char_to_int(roman[i+1])
        
        if next_num == current_num and (current_num == 5 or current_num == 50 or current_num == 500): # En caso de que se repitan los numeros V, L o D, se considera invalido
            return -1

        if repeat_counter == 2:         # En caso de que se hayan repetido 4 veces el mismo numero, se considera invalido
            return -1
        
        if next_num > current_num:
            if current_num >= roman_char_to_int(roman[i+2]): # En caso de que el numero restado sea mayor o igual al siguiente del siguiente, se considera invalido
                return -1
            
            if current_num == 1 and (next_num != 5 and next_num != 10): # En caso de que el numero I se reste a un numero diferente a V o X, se considera invalido
                return -1
            
            if current_num == 10 and (next_num != 50 and next_num != 100): # En caso de que el numero X se reste a un numero diferente a L o C, se considera invalido
                return -1
            
            if current_num == 100 and (next_num != 500 and next_num != 1000): # En caso de que el numero C se reste a un numero diferente a D o M, se considera invalido
                return -1

            new_num = roman_to_dec(roman, i + 2)
            if new_num == -1:
                return -1
            return (next_num - current_num) + new_num
        else:
            
            if next_num == current_num:
                repeat_counter_aux = repeat_counter
                repeat_counter_aux +=1
            else:
                repeat_counter_aux = 0  # Si el numero siguiente es diferente, se reinicia el contador de repeticiones
                
            new_num = roman_to_dec(roman, i + 1, repeat_counter_aux)
            if new_num == -1:
                return -1
            return current_num + new_num
    else: 
        return current_num


    
    
    

roman_num = input("Ingrese un número romano (todo en mayúsc): ")
dec_num = roman_to_dec(roman_num)
if dec_num != -1:
    print("El numero ",roman_num," se expresa como ",dec_num," en decimal.")
else:
    print("El número ingresado no es valido")