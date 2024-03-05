from tkinter import *
import math

def obtener_resultado(fraccion):
    if '/' in fraccion:
        partes = fraccion.split('/')
        if len(partes) == 2:
            numerador = float(partes[0])
            denominador = float(partes[1])
            resultado = numerador / denominador
            return resultado

def comparar_fracciones(event):
    fraccion = entryFraccion.get()
    resultado = obtener_resultado(fraccion)
    if resultado is not None:
        textoResultado.config(text=str(resultado))
        resultado_python = int(resultado)
        resultado_division = int(resultado)
        
        son_iguales = math.isclose(resultado_division, resultado_python)
        if son_iguales:
            labelComparacion.config(text="Son iguales para Python")
        else:
            labelComparacion.config(text="No son iguales para Python")

# Creación de la ventana
ventana = Tk()
ventana.wm_title("Comparar")
ventana.wm_geometry("250x80")

# Elementos de la interfaz
labelFraccion = Label(ventana, text="Fracción:")
labelFraccion.grid(row=0, column=0)

entryFraccion = Entry(ventana)
entryFraccion.grid(row=0, column=1)
entryFraccion.bind("<Return>", comparar_fracciones)

labelResultado = Label(ventana, text="Resultado:")
labelResultado.grid(row=1, column=0)

textoResultado = Label(ventana, text="")
textoResultado.grid(row=1, column=1)

labelComparacion = Label(ventana, text="")
labelComparacion.grid(row=2, column=0, columnspan=2)

ventana.mainloop()
