"""Realizar un algoritmo que indique el numero menor y el numero mayor entre tres
enteros leidos por consola. Solo se deben ingresar numeros enteros."""

num1 = int(input("ingrese un numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

numero_mayor = max(num1, num2, num3)
numero_menor = min(num1, num2, num3)

print("El numero mayor es: ", numero_mayor)
print("Y el numero menor es: ", numero_menor)
