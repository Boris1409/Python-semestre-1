# Este es un ejemplo de uso para if...else..
# Permite ejecutar diferentes acciones según una condición. Funciona como el SI o SiNo de Pseint
# bash

# x = 5
# if x >= 5:
#     print("x es mayor o igual que 5")
# else:
#     print("x es menor a 5")
# if x == 5:
#     print("x es igual a 5")

odd_numbers = 0
even_numbers = 0
 
number = int(input("Introduce un número o escribe 0 para detener: "))
 
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)
