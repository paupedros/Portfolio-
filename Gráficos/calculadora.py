from tkinter import *
 
raiz = Tk()

miFrame = Frame(raiz)
miFrame.config(bg="#373737")
miFrame.pack()

operacion = ""

resultado = 0

# ------------PANTALLA------------

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, columnspan=4, padx=10, pady=10)
pantalla.config(bg="#4e4e4e",fg="#e7e7e7", justify="right")

# ------------PULSACIONES TECLADO------------

def numeroPulsado(num):
    
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)
    
# ------------FUNCION SUMA------------

def suma(num):
    global operacion
    global resultado
    
    resultado += int(num)
    operacion = "suma"
    
    numeroPantalla.set(resultado)
    
# ------------FUNCION EL_RESULTADO------------

def el_resultado():
    global resultado
    
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0

# ------------BOTONES------------
# --------FILA 1--------

boton7 = Button(miFrame,text="7", width=3, command=lambda:numeroPulsado("7")).grid(row=2, column=0, padx=3, pady=3)
boton8 = Button(miFrame,text="8", width=3, command=lambda:numeroPulsado("8")).grid(row=2, column=1, padx=3, pady=3)
boton9 = Button(miFrame,text="9", width=3, command=lambda:numeroPulsado("9")).grid(row=2, column=2, padx=3, pady=3)
botonDiv = Button(miFrame,text="/", width=3).grid(row=2, column=3, padx=3, pady=3)

# --------FILA 2--------

boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4")).grid(row=3, column=0,padx=3, pady=3)
boton5 = Button(miFrame,text="5", width=3, command=lambda:numeroPulsado("5")).grid(row=3, column=1, padx=3, pady=3)
boton6 = Button(miFrame,text="6", width=3, command=lambda:numeroPulsado("6")).grid(row=3, column=2, padx=3, pady=3)
botonMult = Button(miFrame,text="x", width=3).grid(row=3, column=3, padx=3, pady=3)

# --------FILA 3--------

boton1 = Button(miFrame,text="1", width=3, command=lambda:numeroPulsado("1")).grid(row=4, column=0, padx=3, pady=3)
boton2 = Button(miFrame,text="2", width=3, command=lambda:numeroPulsado("2")).grid(row=4, column=1, padx=3, pady=3)
boton3 = Button(miFrame,text="3", width=3, command=lambda:numeroPulsado("3")).grid(row=4, column=2, padx=3, pady=3)
botonRest = Button(miFrame,text="-", width=3).grid(row=4, column=3, padx=3, pady=3)

# --------FILA 4--------

botonComa = Button(miFrame,text=",", width=3, command=lambda:numeroPulsado(",")).grid(row=5, column=0, padx=3, pady=3)
boton0 = Button(miFrame,text="0", width=3, command=lambda:numeroPulsado("0")).grid(row=5, column=1, padx=3, pady=3)
botonSuma = Button(miFrame,text="+", width=3, command=lambda:suma(numeroPantalla.get())).grid(row=5, column=2, padx=3, pady=3)
botonIgual = Button(miFrame,text="=", width=3, command=lambda:el_resultado()).grid(row=5, column=3, padx=3, pady=3)

raiz.mainloop()