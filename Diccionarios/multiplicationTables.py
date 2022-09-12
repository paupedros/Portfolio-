def table(n):
    resultat = []
    i = n
    while i <= n*10:
        resultat += [i]
        i += n
    return resultat

def multiplicationTables(n):
    resultat = {}
    i = 1
    while i <= n:
        resultat[i] = table(i)
        i += 1
    return resultat

print(multiplicationTables(2))

# Crea un diccionario con las tablas de multiplicar desde el 1 hasta el número n (incluido)