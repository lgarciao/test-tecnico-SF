def find_missing_letter(chars):
    # Se obtiene el valor ASCII de la primera letra del array
    int_char = ord(chars[0])
    
    for x in range(len(chars)):
        # Se va obteniendo la letra del código ASCII
        char = chr(int_char + x)
        
        if chars[x] != char:
            break
    return char