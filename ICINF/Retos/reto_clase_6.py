"""Obtener los números del rango 10 al 30,
incrementando de 2 en 2. A continuación,
sumar todos los números obtenidos."""

sum = 0

for i in range(10, 31, 2):
    sum += i

print("La suma de los números obtenidos es:",sum)
