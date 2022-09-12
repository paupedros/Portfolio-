def filter(l):
    result = []
    for element in l:
        if element > 0:
            result += [element]
    return result

print(filter([1, 2, 3]))

# Filtra la lista y la devuelve con solo los números positivos y mas grandes que 0