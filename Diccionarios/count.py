def count(d):
    i = 0
    for element in d.values():
        if 'a' in element:
            i += 1
    return i

print(count({1: "helalo", 2: "haow", 3: "are", 4: "yoau"}))

# Dado un diccionario devuelve las veces que aparece la letra 'a' en los valores