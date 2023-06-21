"""03-Operadores"""

#01-OPERADORES ARITMETICOS

#Declarando variables de tipo entero
a = 20
b = 5
c = 4
d = 20

#Operaciones Comunes
print("       01-OPERADORES ARITMETICOS  ")

print("\nSuma entre a + b es:",a + b)
print("Resta entre a - b es:",a - b)
print("Multiplicación entre a * b es:",a * b)
print("División entre a / b es:",a / b)
print("El módulo entre a y b es:",a % b)
print("El cociente entre b / c es:",b // c)
print("El resultado de b elevado a c (5^4):",b ** c,"\n")

#Declarando variables de tipo flotantes
t = 5.39 #tiempo en segundos
g = 9.81 #la aceleración de gravedad

#Operaciones aritemeticas con flotantes
v = g * t

print(f"La velocidad del objeto en caida libre es de: {v} m/s")
print("La velocidad del objeto en caida libre es de: {:.2f}".format(v)) #1 manera de formatear decimales
print(f"La velocidad del objeto en caida libre es de: {v:.2f}")         #2 manera de formatear decimales con f-string
print("La velocidad del objeto en caida libre es de:","%.2f" % v)       #3 utilizando el formateador %f
print("\n")

#Declarando variables de tipo compleja
c1 = 4 + 3j
print(type(c1))

#Creando un número complejo con complex
c2 = complex(3, -5)

print("El numero complejo es:",c2)

print(c2.real) #Obteniendo la parte real del número complejo
print(c2.imag) #Obteniendo la parte imaginaria del número complejo


#¿Se puede realizar esta operación? ¿Multiplicar un String por un entero?
print("Hola" * 5)

#¿y la siguiente multiplicación?
#print("Hola" * 3.5*2)
#Si el resultado es un 7 (numero entero), ¿por qué sale error?

#¿y esta operación un poco mas elaborada?
print("Hola" * (int((10 * 2) / 5)),"\n")

#¿y por último esta operación de suma?
#print("Hola" + 20)

#02-OPERADORES DE COMPARACIÓN
print("        02-OPERADORES DE COMPARACIÓN ")
print(a == b) #igual a
print(a != b) #desigual a
print(a > b)  #mayor que
print(a < b)  #menor que
print(c >= d) #mayor o igual que
print(c <= d) #menor o igual que

#Comparando cadenas de caracteres
animal_domestico = "gato"
animal_salvaje= "leopardo"
print("\nComparando Cadenas de Caracteres")
print(animal_domestico == animal_salvaje)   #igual a
print(animal_domestico != animal_salvaje)   #desigual a
print(animal_domestico > animal_salvaje)    #mayor que
print(animal_domestico < animal_salvaje)    #menor que
print(animal_domestico >= animal_salvaje)   #mayor o igual que
print(animal_domestico <= animal_salvaje)   #menor o igual que

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

bencina = True
encendido = True
edad = 19

1. #If and
if bencina and encendido:  #El "and" tienen que cumplirse ambas condiciones
    print("El vehiculo puede avanzar","\n")
else:
    print("El vehiculo no puede arrancar","\n")

2. #If or
if bencina  or encendido: #El "or" basta con que se cumpla una condicion 
    print("El vehiculo puede correr,","\n")
else:
    print("El vehiculo no puede arrancar","\n")
    
3. #If not, and
if not bencina and encendido: #El "not" es una contradiccion, si es true = false y si es false = true 
    print("")
else:
    print("El vehiculo no puede arrancar","\n")
    
4. #If not, and
if not bencina or (encendido and edad >= 99):
    print("Esta maquina correra","\n")
else: 
    print("Este tarro ni se movera","\n")
    