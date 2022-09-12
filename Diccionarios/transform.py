def length(l):
    if len(l) == 0:
        return False
    else:
        for element in l:
            count = 0
            for se in l:
                if len(element) == len(se):
                    count += 1
                    if count > 1:
                        return True
        return False

def transform(l):
    dicc = {}
    if length(l):
        return dicc
    else:
        for element in l:
            dicc[len(element)] = element
    return dicc

print(transform(["a", "ab", "abc"]))

# Devuelve el diccionario vacio si dos elementos tienen la misma longitud, si no,
# crea un diccionario con la cadena de valor y su longitud como clave