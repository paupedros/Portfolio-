def lines1(l):
    if len(l) == 0:
        return {}
    else:
        dicc = {}
        count = 0
        for element in l:
            dicc[count] = element
            count += 1
    return dicc

print(lines1(["hello", "how", "are", "you"]))

# Crea un diccionario donde el elemento de la lista es el valor y su posición es la clave