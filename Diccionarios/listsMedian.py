def listsMedian(l):
    if len(l) == 0:
        return 'You can not calculate the median of an empty list'
    else:
        l.sort()
        resultat = []
        for subllista in l:
            poscentral = len(subllista) / 2
            if len(subllista) % 2 != 0:
                resultat = resultat + [subllista[poscentral]]
            else:
                resultat = resultat + [(subllista[poscentral-1] + subllista[poscentral]) / 2.0]
        poscentral = len(resultat) / 2
        if len(resultat) % 2 != 0:
            return resultat[poscentral]
        else:
            return (resultat[poscentral -1] + resultat[poscentral]) / 2.0
        
print(listsMedian([[1.0, 2.0], [8.0, 7.0, 7.0], [2.0, 3.0]]))

# Calcula y devuelve la mediana de varias listas