from tkinter import * # Se usa * para traer todo sobre el paquete tkinter
from tkinter import ttk

# saludar: None -> None
def saludar():
    saludo.config(text="Hola")
    
# greet: None -> None
def greet():
    saludo.config(text = "Hello")

ventana = Tk() #Creamos un objeto de tipo ventana

1. # Button: contenedor str funcion
boton1 = Button(ventana, text="Español", command = saludar)
boton1.pack()

2. # Button: contenedor str funcion
boton2 = Button(ventana, text="Ingles", command = greet)
boton2.pack()

saludo = Label(ventana)
saludo.pack()

ventana.mainloop() #Muestra en pantallala ventana para interactuar 
