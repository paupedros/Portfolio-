def count2(d,c):
    i = 0
    for element in d.values():
        if c in element:
            i += 1
    return i

print(count2({1: "hello", 2: "how", 3: "are", 4: "you"}, 'e'))

# Dado un diccionario devuelve las veces que aparece la variable c en los valores