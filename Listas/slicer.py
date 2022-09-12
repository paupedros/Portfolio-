def slicer(l,n,m):
    if (n< 0) or (m < 0) or (n>len(l)-1) or (m>len(l)-1) or(n>m):
        return []
    else:
        return l[n:m]

print(slicer(["hello", "how", "are", "you"],2,3))

# Corta la lista entre los valores introducidos