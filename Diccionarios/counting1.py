def counting1(s):
    result = {}
    for c in s:
        if result.has_key(c):
            result[c] += 1
        else:
            result[c] = 1
    return result

print(counting1("hello how are you"))

# Crea el diccionario de utilizar cada carácter como clave y el numero de apariciones del mismo como valor