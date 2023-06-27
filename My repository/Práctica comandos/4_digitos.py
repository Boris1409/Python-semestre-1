""" Escribir un programa que al recibir como dato un numero de 4 digitos, genere una impresion como la que se muestra a continuacion:
4
3
2
1
"""

def ingreso_numero():
    while True:
        numero = input('Ingrese un numero de 4 digitos ')
        if len(numero) < 4 or len(numero) > 4:
            print('Ingrese un numero que tenga 4 digitos')
            continue
        else:
            break
    print(numero[0])
    print(numero[1])
    print(numero[2])
    print(numero[3])

numero = ingreso_numero()
