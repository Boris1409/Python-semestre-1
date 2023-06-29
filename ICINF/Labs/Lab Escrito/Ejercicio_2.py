# Se tiene las siguientes tres listas de números enteros:

# a = [10,80,15,30,20]
# b = [20,45,80,20,10]
# c = [20,35,60,90,20]

# Se solicita:
# A) Crear una función para encontrar los valores en común de las tres listas.
# B) Crear una función para concatenar todas las listas en una sola.
# C) Crea una función y eliminar los valores duplicados de la lista anterior.
# D) Crear una función y ordenar la lista de forma descendente.
# E) Crear una función y reemplazar el valor de la posición 7° por el número 100

a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]

# A) Crear una función para encontrar los valores en común de las tres listas.
def valores_comunes(a, b, c):
    val_comunes = list(set(a) & set(b) & set(c))
    return val_comunes

# B) Crear una función para concatenar todas las listas en una sola.
def sumar_listas(a, b, c):
    lista_sum = a + b + c
    return lista_sum

# C) Crea una función y eliminar los valores duplicados de la lista anterior.
def eliminar_dupes(lista_sum):
    lista_wDupes = list(set(lista_sum))
    return lista_wDupes

# D) Crear una función y ordenar la lista de forma descendente.
def ordenar_lista(lista_sin_dup):
    lista_ordenada = sorted(lista_sin_dup, reverse=True)
    return lista_ordenada

# E) Crear una función y reemplazar el valor de la posición 7° por el número 100
def reemplazar_num(lista_ordenada):
    lista_copy = lista_ordenada.copy()
    lista_copy[6] = 100
    return lista_copy

val_comunes = valores_comunes(a, b ,c)
lista_sum = sumar_listas(a, b ,c)
lista_sin_dup = eliminar_dupes(lista_sum)
lista_ordenada = ordenar_lista(lista_sin_dup)
lista_final = reemplazar_num(lista_ordenada)

print(f'Valores en comun de las 3 listas: {val_comunes}')
print(f'Concatenacion de las 3 listas: {lista_sum}')
print(f'Eliminacion de duplicados: {lista_sin_dup}')
print(f'Ordenando la lista de forma descendente: {lista_ordenada}')
print(f'Reemplazando la posicion 7° por un 100: {lista_final}')
