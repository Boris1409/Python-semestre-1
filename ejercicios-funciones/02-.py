#2. # Escribir una función que calcule el área de un círculo y 
# otra funcion que calcule el volumen de un cilindro.

# Area circulo = pi * r**2
# Area cilindro = 2 * pi * r * h * (r + h)
# h = altura

pi = 3.1416

##################################################################

print("\n - CALCULAR EL AREA DEL CIRCULO - ")

def calcular_area_circulo(pi,r): 
    return pi * r ** 2
r = int(input("Ingrese el radio del circulo: "))
print("El area del circulo es de: ",round(calcular_area_circulo(pi,r),2))

##################################################################

print("\n - CALCULAR EL AREA DEL CILINDRO - ")

def calcular_area_cilindro(pi,r):
    return pi * r ** 2    
r = float(input("Ingrese el radio del cilindro: "))
print("El area del cilindro es de: ",round(calcular_area_cilindro(pi,r),2))

###################################################################

print("\n - CALCULAR EL VOLUMEN DEL CILINDRO - ")

def calcular_volumen_cilindro(a,h):
    return a * h
a = calcular_area_cilindro(pi,r)
h = int(input("Ingrese la altura del cilindro: "))
print("El volumen del cilindro es de: ",round(calcular_volumen_cilindro(a,h),2))

###################################################################