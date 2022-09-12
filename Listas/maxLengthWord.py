def maxLengthWord(l):
    if len(l) == 0:
        return -1
    else:
        maxtemp = l[0]
        for element in l:
            if len(element) > len(maxtemp):
                maxtemp = element
            return maxtemp

print(maxLengthWord(['hello', 'how', 'are', 'you']))

# Devuelve la cadena mas larga de la lista