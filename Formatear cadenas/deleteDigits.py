def deleteDigits(s):
    result = ""
    for letter in s:
        if letter not in '0123456789':
            result += letter
    return result

print(deleteDigits("a1sd2v3"))

# Quita los números de la cadena