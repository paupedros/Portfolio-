def correct3(l):
    result = {}
    i = 0
    while i != len(l):
        if '@' in l[i]:
            result[i] = l[i]
        i += 1
    return result

print(correct3(["b", "@bc", "bcd", "@bcd", "abcde"]))

# Devuelve el diccionario con las cadenas que contienen el carácter @,
# estas se utilizan como valor y su posición en la lista se utiliza como clave