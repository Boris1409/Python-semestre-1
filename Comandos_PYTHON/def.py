# def holax(nombre):
#     # input("Ingresa tu nombre: ")
#     print("Ingresa tu nombre:", nombre)

# # nombre = input("Ingresa tu nombre: ")
# holax(2)
# print("Adios")

print("""
      EJEMPLOS DE FUNCIONES
      """)

def num(numero):
    print("Ingresa un numero:", numero)
    
num(93)

def mensaje(que, number):
    print("Ingresa", que, "numero", number)
    
mensaje("telefono", 11)
mensaje("precio", 5)
mensaje("numero", "number")

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

print(adding)

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction()

print(""" 
      FUNCIONES CON 2 ARGUMENTOS
      """)

def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)
 
hi_all("Sebastián", "Konrad")
 
print("""
      FUNCIONES CON 3 ARGUMENTOS
      """)
 
def address(street, city, postal_code):
    print("Tu dirección es:", street,"St.,", city, postal_code)
 
s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)

print("""
      OPERACIONES CON FUNCIONES
      """)
# Ejemplo 1.
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # salida: 3
subtra(2, 5) # salida: -3
 
 
# Ejemplo 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # salida: 3
subtra(b=2, a=5) # salida: 3
 
# Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # salida: 3
subtra(5, 2) # salida: 3

print(""" 
      UNA LISTA A UNA FUNCION COMO ARGUMENTO 
      """)

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))