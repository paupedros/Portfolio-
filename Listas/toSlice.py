def toSlice(s):
    str = s
    result = []
    if len(s) == 0:
        return result
    else:
        result += str.split()
    return result

print(toSlice("hello how are you"))

# Convierte la cadena en una lista con cada palabra separada