"""Construir un programa que al recibir como dato el radio de un circulo, calcule e imprima tanto su area como la longitud de su circunferencia.
° El area de un circuo la calculamos como:
    area = pi * radio^2
° La circunferencia la calculamos como:
    loongitud = 2 * pi * radio 
"""

pi = 3.14

def ingreso_radio():
    radio = float(input('Ingrese el radio del circulo '))
    return radio

def calcular_area(radio):
    area = pi * radio ** 2
    print('El área de la figura es ',area)

def calcular_longitud(radio):
    longitud = 2 * pi * radio
    print('La longitud del radio es ',longitud)

radio = ingreso_radio()
calcular_area(radio)
calcular_longitud(radio)