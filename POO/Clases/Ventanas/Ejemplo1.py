from tkinter import *
from tkinter import ttk
# Se usa * para traer todo sobre el paquete tkinter

ventana = Tk() #Creamos un objeto de tipo ventana
saludo = Label(ventana, text="Hola")

saludo.pack() 
ventana.mainloop()