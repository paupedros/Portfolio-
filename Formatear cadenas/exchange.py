def exchange(s,a,b):
    if (a < 0 or b < 0 or a >= len(s) or b >= len(s)):
        return s
    i = 0
    result = ""
    while i < len(s):
        if i == a:
            result = result + s[b]
        elif i == b:
            result = result + s[a]
        else:
            result = result + s[i]
        i = i + 1
    return result

print(exchange("hello",3,4))

# Cambia los caracteres de la cadena que ocupan las posiciones a y b