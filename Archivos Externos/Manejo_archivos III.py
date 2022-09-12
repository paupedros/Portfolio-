from io import open_code

archivo_texto = open("archivo.txt", "r")

lineas_texto = archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)



