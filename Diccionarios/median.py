def median(l):
    if len(l) == 0:
        return "You can not calculate the median of an empty list"
    else:
        l.sort()
        poscentral = len(l) /2
        if len(l) % 2 != 0:
            return l[poscentral]
        else:
            return (l[poscentral - 1] + l[poscentral]) / 2
    
print(median([1.0,2.0,0.5]))

# Calcula y devuelve la mediana de la lista