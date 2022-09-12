from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

# ------------ VARIABLES ------------

miNombre = StringVar()

# ------------ ENTRIES / CUADROS DE TEXTO ------------

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red", justify="left")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)

# ------------ TEXTO ------------

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4,column=1)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="NSEW")

textoComentario.config(yscrollcommand=scrollVert.set)

# ------------ LABELS ------------

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", pady=10, padx=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0, sticky="e", pady=10, padx=10)

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3,column=0, sticky="e", pady=10, padx=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=1,column=0, sticky="e", pady=10, padx=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4,column=0, sticky="e", pady=10, padx=10)

# ------------ BUTTONS ------------

def codigoBoton():
    miNombre.set("Pau")

botonEnvio = Button(miFrame,text="Enviar", command=codigoBoton)
botonEnvio.grid(row=6,column=1,sticky="e", pady=10)
botonEnvio.config(relief="solid", cursor="hand2")


raiz.mainloop()