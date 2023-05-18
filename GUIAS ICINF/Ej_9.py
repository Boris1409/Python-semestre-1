"""Se tiene la siguiente lista de enteros:
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
Se solicita:
a) Eliminar el ultimo elemento de la lista
b) Agregar en la primera posicion el numero 2
c) Eliminar los numeros duplicados de la lista
d) Obtener la media y la mediana de la lista"""

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
print(numeros)

numeros.pop()
print(numeros)

numeros.insert(0,2)
print(numeros)

numeros = list(set(numeros))
print(numeros)

import statistics

media = statistics.mean(numeros)
mediana = statistics.median(numeros)

print(numeros)
print("La media de la lista es: ",media)
print("La mediana de la lista es: ",mediana)