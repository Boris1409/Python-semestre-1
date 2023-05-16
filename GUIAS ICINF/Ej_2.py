"""Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
dos variables diferentes. Luego imprimir cual palabra tiene mas caracteres y cual
tiene menos caracteres"""

var1 = input("Escriba una palabra: ")
var2 = input("Escriba otra palabra: ")

# mayor = max(var1), (var2)
# menor = min(var1), (var2)

if len(var1) > len(var2):
    print("La palabra con mas caracteres es: ", var1)
else:
    print("La palabra con menos caracteres es: ", var2)