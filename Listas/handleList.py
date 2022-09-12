def deletedigits(s):
    result= ""
    for c in s:
        if c not in "0123456789":
            result += c
    return result
    
def handleList(l):
    resultat= []
    for element in l:
        if len(element) > 3:
            resultat += [deletedigits(element)]
        else:
            resultat += [element]
    return resultat

print(handleList(["a", "1", "abcd", "1234", "a1b", "a1b2c3"]))

# Elimina los números en esos elementos que tengan más de 3 caracteres