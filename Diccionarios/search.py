def search(d,n):
    if n in d.values():
        return True
    else:
        return False
    
search({"one": 1, "two": 2, "three": 3}, 3)

# Devuelve True si n esta dentro de los valores del diccionario