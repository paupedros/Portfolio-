from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

# ------------ ENTRIES / CUADROS DE TEXTO ------------

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red", justify="left")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)

# ------------LABELS------------

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", pady=10, padx=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0, sticky="e", pady=10, padx=10)

direccionLabel = Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=3,column=0, sticky="e", pady=10, padx=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=1,column=0, sticky="e", pady=10, padx=10)


raiz.mainloop()