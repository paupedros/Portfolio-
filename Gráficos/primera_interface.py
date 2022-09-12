from tkinter import *

raiz = Tk()

raiz.title("Ventana de cacas")
raiz.iconbitmap('graficos\icons\icon.ico')
raiz.resizable(1,1)
#raiz.geometry("650x350")
raiz.config(bg="coral")
raiz.config(bd="10")
raiz.config(relief="groove")


miFrame = Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="650",height="350")
miFrame.config(bd=10)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")




raiz.mainloop()

