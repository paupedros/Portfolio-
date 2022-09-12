def encode4(s,n):
    result= ""
    for letter in s:
        if ord(letter) + n > 122:
            result += chr(96 + n - (122 - ord(letter)))
        else:
            result = result + chr(ord(letter)+n)
    return result

print(encode4("hadagsdbigazxcewy",15))

# Le suma a cada carácter de la cadena el valor de n en la tabla Ascii