from io import open_code

archivo_texto = open("archivo.txt", "r")

archivo_texto.seek(len(archivo_texto.readline()))
# El cursor se situa al final de la primera linia

print(archivo_texto.read())
