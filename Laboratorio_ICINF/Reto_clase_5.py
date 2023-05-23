"""Hacer un algoritmo que detecte si un número es
par o impar, además si es un número primo y si es
mayor o menor a 50. Para este ejercicio se solicita
utilizar condicionales y bucles."""

while True:
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        print("No se aceptan numeros negativos, ingrese otra vez el numero.")
    else:
        break
    
print("El número es primo." if numero % 2 != 0 else "El numero no es primo.")
print("El número es par." if numero % 2 == 0 else "El número es Impar.")
print("El número es mayor a 50" if numero > 50 else "E número no es mayor a 50")
