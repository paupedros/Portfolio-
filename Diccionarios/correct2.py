def validate(s):
    for c in s:
        if c in 'aeiouAEIOU':
            return True
        return False

def correct2(l):
    result = {}
    i = 0
    for element in l:
        if validate(element):
            result[i] = element
        i += 1
    return result

print(correct2(["b", "bc", "bcd", "abcd", "abcde"]))

# Devuelve la posición como clave de las cadenas que
# contienen una vocal i como valor la misma cadena