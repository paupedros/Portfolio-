def minIntegerList(l):
    if len(l) == 0:
        return 'There is no minimum'
    else:
        mintemp = l[0]
        for num in l:
            if num < mintemp:
                mintemp = num
        return mintemp

print(minIntegerList([1,2,3,8,0]))

# Devuelve el elemento entero más pequeño de la lista