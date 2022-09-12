def dictioLists(l):
    result = {}
    for element in l:
        result[element[-1]] = element
    return result

print(dictioLists([["how", "are", "you"], ["a"], ["1", "2"]]))

# Devuelve un diccionario a partir de una lista de sublistas, donde la
# clave es el ultimo elemento y el valor la sublista