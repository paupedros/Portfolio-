def deleteLowerCase(s):
    result=""
    for letter in s:
        if 'A'< letter and letter< 'Z':
            result += letter
    return result

print(deleteLowerCase("HellO"))

# Elimina de la cadena los caracteres en minúscula