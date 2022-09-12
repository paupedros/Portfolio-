def sliceBetweenValues(s,n,m):
    if (n<0 or m<0 or n>=len(s) or m>=len(s)):
        return ""
    elif (n>=m or m == 0):
        return ""
    else:
        return s[n:m]
    
print(sliceBetweenValues("hello", 0, 5))

# Corta la cadena entre dos valores