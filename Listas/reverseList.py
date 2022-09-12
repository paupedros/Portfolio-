def reverseList(l):
    result = []
    i = len(l)-1
    while i >= 0:
        result += [l[i]]
        i = i-1
    return result
                    
print(reverseList(['you', 'are', 'how', 'hello']))

# Devuelve la lista al revés