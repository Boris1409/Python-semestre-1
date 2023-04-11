"""Este es un ejemplo de uso de la libreria de python"""

#01-DATOS DE TIPO NUMÉRICO

estatura = 1.89
peso = 70
complejo = 1+4j

print("Impresion del número complejo:", complejo)

#OPERACION ARITMETICA BÁSICA 

imc = peso/estatura**2
imc = 1.89/70**2
print(imc)

"""------------------------------------------------------------------------------------------------------------------"""

#02- DATOS DE TIPO CADENA DE CARACTERES

asignatura = "Programación"
carrera = "Ingeniería Civil Informatica"

"""------------------------------------------------------------------------------------------------------------------"""

#O3 VALORES BOOLEANOS
ampolleta = False
interruptor = True


#TYPE SABEMOS EL TIPO DE DATO QUE ESTAMOS TRATANDO

print(type(ampolleta))

"""------------------------------------------------------------------------------------------------------------------"""

#04- DATOS TIPO ARRAY (OBJETOS DE TIPO COLECCION)

estudiantes = ("Matias", "Marco", "Cristobal", "Sebastian")
num = (1,2,3,4,5,6)
print(estudiantes)
print(num)


# Clase 11 de Abril

Estatura =  1.70
peso = 70
complejo = 1+4j

print(f"Mi estatura es de {estatura} y mi peso es de {peso}")

# OPERACIÓN ARITMÉTICA
imc = peso/estatura**2

print("mi IMC es de: {:.2f}" .format(imc), "\n")

print(type(Estatura))

print("##### 04-LISTAS ########")

#DECLARANDO LISTAS

estudiantes = ["Matias, Cristian, Franco, Boris"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]

print(estudiantes, num, lenguaje)
print("\n")
print(type(estudiantes))
print("\n")
print(len(num))
print("\n")

data = ["Osorno", {"UV": "nivel bajo", "Temp °C": 15}, (-40.5735,29)]
print(type(data))
#FUNCIONES PROPIAS DE PYTHON STR() INT() FLOAT() LEN() TYPE() COUNT("DIEGO")

lenguaje = ["JavScript"]

data_asig = [10023, "Programación",1,True]
cod,ramo,semestre,estado, = data_asig
print(ramo)
print("\n")

#¿Se podrán sumar listas?
a=[1,2,3,4]
b=["Boris",True,100]
print("Suma de listas", estudiantes + num)
print("\n")
print(list("Python"))
print("\n")
print(list(range(10)))
print("\n")
