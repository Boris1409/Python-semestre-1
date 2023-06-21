# Este es un ejemplo de uso listas 
# Permiten almacenar una colección de elementos.

# numeros = [1, 2, 3, 4, 5]
# print(numeros[0])

num = [10, 5, 7, 2, 1]
print("EL contenido de la lista es: ", num)

num[4] = 992
print("\nPrevio contenido de la lista es: ", num)

num[1] = num[4] #Copia el valor del quinto elemento al segundo elemento de la lista

print("\nNuevo contenido de lista: ",num)
print("\Longitud de la lista es: ",len(num))
print(num[2]) # Imprime el valor del segundo elemento 
print(num)
print("\n")

del num[1]

print(len(num))
print(num)