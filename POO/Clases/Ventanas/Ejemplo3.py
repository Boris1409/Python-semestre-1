from tkinter import * # Se usa * para traer todo sobre el paquete tkinter
from tkinter import ttk

# saludar: str -> None
def saludar(s):
    s = nombre.get()
    saludo.config(text="Hola " + s)
    
# greet: None -> None
def greet():
    saludo.config(text = "Hello")

ventana = Tk() #Creamos un objeto de tipo ventana

pregunta = Label(ventana, text="¿Cual es tu nombre?")
pregunta.pack()

# Entry: contenedor -> None
nombre = Entry(ventana)
nombre.pack()
nombre.bind("<Return>", saludar)

saludo= Label(ventana, text="Hola")
saludo.pack()

ventana.mainloop() #Muestra en pantallala ventana para interactuar 