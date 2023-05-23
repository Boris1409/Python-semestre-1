def saludo(nombre):
    print("Hola {}".format(nombre))
    
saludo("Boris")

""""""""""""""""""""""""""""""""""""""""""""

def multiply(a, b):
    return a * b
 
print(multiply(3, 4)) # salida: 12
 
 
def multiply(a, b):
    return
 
print(multiply(3, 4)) # salida: None

""""""""""""""""""""""""""""""""""""""""""""

def wishes():
    return "¡Felíz Cumpleaños!"
 
w = wishes()
 
print(w) # salida:¡Felíz Cumpleaños!
 
""""""""""""""""""""""""""""""""""""""""""""

# Ejemplo 1
def wishess():
    print("Mis deseos")
    return "Felíz Cumpleaños"
 
wishess() # salida: Mis deseos
 
 
# Ejemplo 2
def wishess():
    print("Mis deseos")
    return "Felíz Cumpleaños"
 
print(wishess())
 
# salida: Mis deseos
# Felíz Cumpleaños
 
""""""""""""""""""""""""""""""""""""""""""""

def hi_everybody(my_list):
    for name in my_list:
        print("Hola,", name)
 
hi_everybody(["Adán", "Juan", "Lucía"])

""""""""""""""""""""""""""""""""""""""""""""

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(create_list(5))
 
 