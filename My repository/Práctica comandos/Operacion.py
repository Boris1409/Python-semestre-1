""" Crear un programa que al recibir como datos dos numeros enteros calcule la suma, resta, multiplicacion y division de dichos numeros """
def ingreso_numeros():
    n1 = float(input('Ingrese el primer numero: '))
    n2 = float(input('Ingrese el segundo numero: '))
    return n1,n2

def suma(n1, n2):
        suma = n1 + n2
        print('La suma de ambos numeros es: ',suma)

def resta(n1,n2):
    resta = n1 - n2
    print('La resta de ambos numeros es: ',resta)

def multiplicacion(n1,n2):
    multiplicacion = n1 * n2
    print('La multiplicacion de ambos numeros es: ',multiplicacion)

def division(n1,n2):
    if n2 != 0:
        division = n1 / n2
        print('La division de ambos numeros es: ',division)
    else:
        print('ERROR MATEMATICO, NO SE PUEDE DIVIDIR ENTRE CERO')

n1,n2 = ingreso_numeros()
suma(n1,n2)
resta(n1,n2)
multiplicacion(n1,n2)
division(n1,n2)