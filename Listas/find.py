def contains(s,c):
    return (c in s)

def find(l,c):
    for element in l:
        if contains(element, c):
            return element
    return ""

print(find(['hallo','e'], 'e'))

# Devuelve el elemento de la lista que contiene c