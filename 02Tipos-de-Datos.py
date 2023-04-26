"""Este es un ejemplo de uso de la libreria de python"""

#01-DATOS DE TIPO NUMÉRICO

estatura = 1.89
peso = 1900.98
complejo = 1+4j

print("Impresion del número complejo:", complejo, "\n")
print("Transformando el numero real a enterooooo", int(peso), "\n")

#OPERACION ARITMETICA BÁSICA 

imc = peso/estatura**2
imc = 1.89/70**2
print("Mi IMC es de: {:.3f}".format(imc), "\n") 
# Con el .format nos sirve para darle un formato a numeros decimales, si queremos que tenga 1 decimal, 2 decimales, etc. su sintaxis es "{:."Numero"f}".format

"""------------------------------------------------------------------------------------------------------------------"""

#02- DATOS DE TIPO CADENA DE CARACTERES

asignatura = "Programación"
carrera = "Ingeniería Civil Informatica"
print("La asignatura de programación tiene un total de:",len(asignatura),"caracteres", "\n") #la funcion "len" permite contabilizar cuantos elementos tiene un string/lista

"""------------------------------------------------------------------------------------------------------------------"""

#O3 VALORES BOOLEANOS
Ampolleta = ("Ampolleta")
ampolleta = False #False siempre sera 0
interruptor = True #True siempre sera 1
print("El valor de la ampolleta es: ", ampolleta)
print("El valor del interruptor es: ", interruptor)
print("El valor de la ampolleta es: ", int(ampolleta))
print("El valor del interruptor es: ", int(interruptor))
print("Ampolleta tiene un total de: ", len(Ampolleta), "caracteres")


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

"""---------------------------------------------------------------------------------------------------------------------------------------"""

print("##### 04-LISTAS ########")

#DECLARANDO LISTAS

estudiantes = ["Matias", "Cristian", "Franco", "Boris","Jordan"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]
nueva_lista = list()
otra_lista = []

print("\n")
print(estudiantes[4])
print("\n")
print(estudiantes, num, lenguaje)
print("\n")
print("Estudiantes es de tipo:",type(estudiantes))
print("Estudiantes tiene un resultado de:",len(estudiantes),"caracteres")
print("\n")
print("Num tiene un total de:", len(num),"caracteres")
print("Num es de tipo:",type(num))
print("\n")
print("Lenguaje es de tipo:",type(lenguaje))
print("Lenguaje tiene un total de:",len(lenguaje),"caracteres")
print("\n")
print("nueva_lista es de tipo:",type(nueva_lista))
print("nueva_lista tiene un total de:",len(nueva_lista), "caracteres")
print("\n")
print(type(otra_lista))
print("\n")

data = ["Osorno", {"UV": "nivel bajo", "Temp °C": 15}, (-40.5735,29)]
print(type(data))
print(data)
#FUNCIONES PROPIAS DE PYTHON STR() INT() FLOAT() LEN() TYPE() COUNT("DIEGO")

lenguaje = ["JavScript"]

data_asig = [10023, "Programación",1,True]
cod,ramo,semestre,estado, = data_asig
print(cod)
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

#05 TUPLAS NO SON MUTABLES
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("####### 05-TUPLAS #####")
print(type(grupo1))

#Accediendo al primer elemento  de la tupla 

print(grupo1[0])
#Consultando el elemento Daniel cuantas veces se encuentra en la lista

print("El elemento se repite:", grupo1.count("Daniel"))

print("Indice del elemento", grupo1.index ("Daniel"))

# grupo1[0] =  "Constanza"
# print(grupo1)
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Daniel" "Alejandra")
print(grupo1[2:5])

conjunto_vacio = set()
print(type(conjunto_vacio))
conjunto_colores = set(["Azul","Rojo","Verde"])
conjunto_animales = {"Gato", "Perro", "Loro"}

print("##### 06-SETS#####")
print(type(conjunto_colores))
print(type(conjunto_animales))
print("El primer set contiene los siguientes colores:",conjunto_colores)
print("El segundo set contiene los siguientes animales:",conjunto_animales)

# print(conjunto_animales{0})

conjunto_colores.add("Celeste")
print("El set de colores lo conforman:",conjunto_colores)
conjunto_colores.add("Pato")
print("El set de animales lo conforman:",conjunto_animales,"\n") 
#la funcion int sirve para transformar un entero a decimal
# la funcion float sirve para agregarle un decimal a un entero














































