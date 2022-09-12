def toDictionary(l):
    if len(l) == 0:
        return {}
    else:
        dicc = {}
        for element in l:
            dicc[element[0]] = element[1]
        return dicc

print(toDictionary([["a", "b"], ["c", "d"]]))

# Transforma una lista con sublistas de cadenas en un diccionario donde
# donde la primera posición de la sublista se utiliza como clave y la segunda como valor