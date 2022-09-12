def counting4(s):
    result = {}
    for c in s:
        if not ('0' <= c and c <= '9') and not ('A' <= c and c <= 'z'):
            if result.has_key(c):
                result[c] = result[c] + 1
            else:
                result[c] = 1
    return result

print(counting4("hello@"))

# Guarda en un diccionario; como clave las veces que se repite un 
# carácter no alfabético y no dígito y como clave el carácter