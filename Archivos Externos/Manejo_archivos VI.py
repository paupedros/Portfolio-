from io import open_code

archivo_texto = open("archivo.txt", "r")

archivo_texto.seek(len(archivo_texto.read())/2)
# El cursor se situa a la mitad del texto

print(archivo_texto.read())
