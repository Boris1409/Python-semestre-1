import numpy as np

lista_1= []
lista_2 = []

print(" ====== EJERCICIO N° 2 ====== ")

numero = int(input("Ingrese el limite de numeros que seran agregados a las dos listas: "))

for i in range(numero):
    numeros = float(input("Escriba un numero para la lista_1: "))
    lista_1.append(numero)

for i in range(numero):
    numeros = float(input("Escriba un numero para la lista_2: "))
    lista_2.append(numero)

def multiplicacion_listas(lista_1, lista_2):
    resultado = []
    for i in range(len(lista_1)):
        resultado.append(lista_1[i] * lista_2[i])
    return resultado

def division_listas(lista_1, lista_2):
    resultado = []
    for i in range(len(lista_1)):
        if lista_2[i] != 0:
            resultado.append(lista_1[i] / lista_2[i])
        else:
            resultado.append(float('inf'))  
    return resultado

def promedio(lista_1, lista_2):
    lista_combinada = lista_1 + lista_2
    promedio = np.mean(sum(lista_combinada) / len(lista_combinada))
    return promedio

def mediana(lista_1, lista_2):
    lista_combinada = lista_1 + lista_2
    lista_combinada.sort()
    numero= len(lista_combinada)
    if numero % 2 == 0:
        mediana = np.median((lista_combinada[numero // 2 - 1] + lista_combinada[numero // 2]) / 2)
    else:
        mediana = np.median(lista_combinada[numero // 2])
    return mediana


resultado_multiplicacion = multiplicacion_listas(lista_1, lista_2)
resultado_division = division_listas(lista_1, lista_2)
promedio = promedio(lista_1, lista_2)
mediana = mediana(lista_1, lista_2)

print("\n ====== RESULTADOS =====")

print("Así es el resultado de la multiplicación:", resultado_multiplicacion)
print("Así es el resultado de la división:", resultado_division)
print("Este es el promedio de las listas combinadas:", promedio)
print("Esta es la mediana de las listas combinadas:", mediana)

print("\n ======== EJERCICIO FINALIZADO ========= ")


""" Calculado el promedio y mediana con numpy """
# promedio = np.mean( )
# mediana = np.median( )
