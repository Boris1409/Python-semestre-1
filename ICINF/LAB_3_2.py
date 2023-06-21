a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

# Concatenar todas las listas e imprimir la lista obtenida

conc = a + b + c
print(conc)

# Agregar el número 20 en la penúltima posición de la lista.

conc.insert(-1, 20)
print(conc)

# Ordenar la lista de forma descendente

conc.sort(reverse=True)
print(conc)

# Insertar la lista [4,5,6] en la última posición de la lista ordenada

n_lit = [4,5,6]
conc.extend([4, 5, 6])
print(conc)

# Sumar todos los números dentro de la lista.

suma = sum(conc)
print("La suma total de la lista es:",suma)

# Obtener el promedio simple de la lista

promedio = suma /len(conc)
print(promedio)
