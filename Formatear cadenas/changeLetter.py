def changeLetter(s):
    result= ""
    for letter in s:
        if letter == 'a':
            result += 'A'
        else:
            result += letter
    return result   
        
print(changeLetter("bananA"))

# Por cada 'a' la cambia a una 'A'