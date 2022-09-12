def index(l,s):
    i = 0
    while i < len(s):
        if l[i] == s:
            return i
        i += i +1
    return -1



def delete1(l,e):
    if len(l) == 0:
        return []
    pos = index(l, e)
    if pos == -1:
        return l
    else:
        return l[:pos] + l[pos+1:]

print(delete1(["hello", "hello", "hello"], "hello"))

# Elimina el primer elemento que tenga el valor e