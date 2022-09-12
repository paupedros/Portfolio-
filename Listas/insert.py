def insert(l,e,n):
    if (n<0) or (n > len(l)-1):
        return l + [e]
    else:
        slice1= l[0:n]
        slice2= l[n:len(l)]
    return slice1 + [e] + slice2

print(insert(["hello", "how", "are", "you"], "bye", 3))

# Inserta como elemento el valor de *e* en la posición *n*