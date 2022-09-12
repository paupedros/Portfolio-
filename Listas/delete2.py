def delete2(l,e):
    result = []
    for element in l:
        if element != e:
            result += [element]
    return result

print(delete2(["bye", "hello", "hello"], "hello"))

# Elimina todos los elementos con el valor de e