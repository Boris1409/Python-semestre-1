"------------------Apuntes Semana 13 -------------------------"

# Examinar y analizar un modelo resulta considerablemente más sencillo.

# Se realiza una abstracción focalizándose exclusivamente en los elementos pertinentes.

# Concepto de Objeto: combinación de estado y función.

# Ejemplo:
# Objeto: Automóvil
# Estado: Nivel de combustible, año de fabricación, color, transmisión automática/mecánica, cilindrada, etc.
# Funcionalidad: Acelerar, frenar, encender el motor, etc.
# Clase:
# Plantilla genérica que sirve como base para la creación de objetos.
# Facilita la concepción y diseño de objetos.
s = "hola"
i = 11
print(type(s))  # Ambos son instancias de clases, s y i

"---------------------------------------------------------------------"
# Interactuando con objetos a través de mensajes.
# Ejemplo: Para un objeto de tipo cadena (string), el mensaje lower(…) implica: "entrega tu contenido en minúsculas".
mensaje = "OLA"
mensaje_en_minusculas = mensaje.lower()
print(mensaje_en_minusculas)

"- - - - - - - - - - Función find() - - - - - - - - - -"

# Ejemplo 1: Solicitar al objeto de texto la posición de la primera aparición de 'ola'.
texto = "Hola Martin. Hay muchas olas."
posicion_primera_aparicion = texto.find("ola")
print(posicion_primera_aparicion)  # Devolverá 1

# Ejemplo 2: Solicitar al objeto de texto la posición de 'ola' desde la posición 3.
posicion_desde_tercera = texto.find("ola", 3)
print(posicion_desde_tercera)  # Devolverá 24

"""-------------------------------------- Ejemplo del auto -----------------------------------------"""

# Clase Auto:
# atributos:
# bencina: int
class Auto:
    
    def __init__(self,bencina):
        self.bencina = bencina
        print(f"Este auto tiene {bencina} litros de bencina")
        
    def arrancar(self):
        if self.bencina>0:
            return "Arranca"
        else:
            return "No arranca"
    
    def conducir(self):
        if self.bencina>0:
            self.bencina-=1
            return f"Quedan {self.bencina} litros"
        else:
            return "No se mueve"
        
        
auto_mio=Auto(3)
print(auto_mio.arrancar())
print(auto_mio.conducir())
print(auto_mio.conducir())
print(auto_mio.conducir())
print(auto_mio.conducir())

"""---------------------------------------- CLASE 09-11-2023 -----------------------------------------------"""

def dialogo():
    print("Suma y mayor de fracciones a/b y c/d")
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    d = int(input("d? "))
    print(f"suma = {suma_fracciones(a,b,c,d)}")
    print(f"mayor = {comparacion_fracciones(a,b,c,d)}")
    
def suma_fracciones(a,b,c,d):
    numerador = (a*d+c*b)
    denominador = b*d
    fraccion = (f"{numerador}/{denominador}")
    return fraccion

def comparacion_fracciones(a,b,c,d):
    if a*d > c*b:
        return f"{a}/{b}"
    else: 
        return f"{c}/{d}"
dialogo()

""" ---------------------------------------- EJEMPLO DEL GATO ----------------------------------------------"""

def dialogo():
    print("Suma y mayor de fracciones a/b y c/d")
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    d = int(input("d? "))
    print(f"suma = {suma_fracciones(a,b,c,d)}")
    print(f"mayor = {comparacion_fracciones(a,b,c,d)}")
    
def suma_fracciones(a,b,c,d):
    numerador = (a*d+c*b)
    denominador = b*d
    fraccion = (f"{numerador}/{denominador}")
    return fraccion

def comparacion_fracciones(a,b,c,d):
    if a*d > c*b:
        return f"{a}/{b}"
    else: 
        return f"{c}/{d}"
dialogo()
