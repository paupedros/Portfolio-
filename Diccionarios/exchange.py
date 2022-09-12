def exchange(d):
    result = {}
    
    for element in d.items():
        result[element[-1]] = element[0]
    return result

print(exchange({"one": 1, "two": 2, "three": 3}))

# Intercambia las claves por los valores del diccionario