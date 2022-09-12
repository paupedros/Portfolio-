def maximum(l):
    return max(l)

def results2(l):
    result = {}
    x = 0
    while x < len(l):
        result[str(l[x])] = maximum(l[x])
        x += 1
    return result

print(results2([[1, 2, 3], [10, 20], [100, 100, 100, 100]]))

# Crea un diccionario donde el maximo numero de la sublista se utiliza
# como valor y la posicion de la sublista como clave