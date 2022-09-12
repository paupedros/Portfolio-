from io import open_code

archivo_texto = open("archivo.txt", "w")

frase = "Estupendo dia para estudiar Python \n el sabado"

archivo_texto.write(frase)

archivo_texto.close()

