from tkinter import *

# clase CalculadoraIMC
# atributos: ventana = objeto
class CalculadoraIMC:
    
    # Se define el metodo '__init__' 
    # Constructor: objeto -> Establece la interfaz grafica del usuario
    # Toma la instancia de ventana para poder formar los widgets basicos, etiquetas y un boton
    def __init__(self, ventana):
        
        # Configurar la pantalla principal
        self.ventana = ventana
        ventana.title("Calculadora de IMC")
        
        # Se crean los elementos visibles de la interfaz grafica. 
        # Usando etiquetas(Label).
        self.label_peso = Label(ventana, text="Introduce tu peso en kg:")
        self.label_peso.pack()

        # Cuadros de entrada(Entry).
        self.entry_peso = Entry(ventana)
        self.entry_peso.pack()

        # Usando etiquetas(Label).
        self.label_altura = Label(ventana, text="Introduce tu altura en m:")
        self.label_altura.pack()

        # Cuadros de entrada(Entry).
        self.entry_altura = Entry(ventana)
        self.entry_altura.pack()
        
        # Y para ingresar los datos un boton(Button) que calcula el IMC.
        self.button_calcular = Button(ventana, text="Calcular IMC", command=self.calcular_imc)
        self.button_calcular.pack()

        # Y muestra con una etiqueta adicional el resultado.
        self.label_resultado = Label(ventana, text="")
        self.label_resultado.pack()

    # Se define el metodo calcular_imc que realiza el calculo del IMC y muestra en una etiqueta el resultado 
    # calcular_imc: float, float -> Indice de masa corporal
    # realiza el calculo del IMC a partir de las entradas de peso y altura y maneja posibles errores si se introducen valores no numericos
    # ejemplo: peso= 69, altura= 1.89 -> Tu IMC es de 19.32
    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            imc = peso / altura ** 2
            resultado = f"Tu índice de masa corporal es: {imc:.2f}"
            self.label_resultado.config(text=resultado)
        except ValueError:
            self.label_resultado.config(text="Por favor, introduce valores numéricos.")

# Se crea una instancia de la clase Tk()
ventana = Tk() 

# Se crea una instancia de la clase 'CalculadoraIMC' pasando la instancia de ventana como argumento
# del constructor de la clase
app = CalculadoraIMC(ventana)

# Configurar el tamaño de la ventana(widht, height)
ventana.resizable(True, False)

# Fijar el tamaño de la ventana
ventana.geometry("275x190")

# Se inicia el bucle con la ventana principal de tkinter 
ventana.mainloop()
