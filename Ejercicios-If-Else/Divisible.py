"""Verificar si un número es divisible por otro"""

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
resto = (dividendo/divisor)

if dividendo % divisor == 0:
    print("El número ", dividendo, "si es divisible por ", divisor)
else:
    print("El número ", dividendo, "no es divisible por ", divisor) 
    
print("Y el resto del procedimieto es ", round(resto, 1))
    