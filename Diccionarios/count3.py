def count3(d,c):
    i = 0
    for element in d.keys():
        if c in element:
            i += 1
    for element in d.values():
        if c in element :
            i += 1
    return i

print(count3({"hello": "hola", "bye": "que", "hi": "tal"}, 'e'))

# Dado un diccionario devuelve las veces que aparece la variable c