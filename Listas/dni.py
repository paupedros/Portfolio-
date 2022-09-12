def dni(l):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    residu = l%23
    return letters[residu]

print(dni(36526775))

# Devuelve la letra del dni correspondiente