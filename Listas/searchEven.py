def searchEven(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            return i
        i += 1
    return -1

print(searchEven([1, 7, -15, 21]))

# Devuelve la posición del primer numero par de la lista, si no hay ninguno devuelve -1