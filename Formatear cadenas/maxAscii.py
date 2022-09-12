def maxAscii(s):
    result=''
    i=0
    for letter in s:
        while i != len(s):
            result= chr(ord(s[i]))
            i += 1
    return result        
            
print(maxAscii('hello'))

# Devuelve el carácter de la cadena con mayor valor en la tabla Ascii