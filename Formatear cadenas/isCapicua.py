def isCapicua(s):
    n= len(s)-1
    m= 0
    while n > m:
        if s[n] == s[m]:
            n -= 1
            m += 1
        else:
            return False
    return True
        
print(isCapicua("hello"))

# Nos devuelve True si la cadena es capicúa