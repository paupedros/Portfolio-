from importlib.resources import path
from tkinter import *

root = Tk()
root.title("practicaLabel")

miFrame = Frame(root,width=500, height=400)
miFrame.pack()

miImagen = PhotoImage(file='graficos\icons\Bell_gongs.gif')

Label(miFrame, text="Hola Mundo!", fg="red", font=("Helvetica", 18)).place(x=100,y=50)
Label(miFrame, image=miImagen).place(x=100,y=100)


root.mainloop()

