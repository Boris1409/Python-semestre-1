"""Determinar si una palabra ingresada por teclado es una palíndromo"""

while True:
    palabra = input("Ingrese una palabra y le diremos si es un palindromo o no: ")
    if palabra.isdigit():
        print("No se aceptan numeros, solo letras")
        continue
    else:
        break
print("La palabra si es un palindromo") if palabra[0] == palabra[-1] else print("La palabra no es un palindromo")