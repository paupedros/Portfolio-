from io import open_code

archivo_texto = open("archivo.txt", "r+")   # r+ indica que el archivo se abrira en modo lectura y escritura

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines();

lista_texto[1] = "Esta linea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
