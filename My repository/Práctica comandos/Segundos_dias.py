""" Construir un programa que calcule e imprima el numero de segundos que hay en un determinado numero de dias.
Dato: DIA (variable de tipo entero que representa el numero de dias)"""

dia      = 24
minutos  = 60
segundos = 60 

def ingreso_dias():
    dia = int(input('Ingrese la cantidad de dias para calcular: '))
    return dia

def segundos_dias(dia):
    seg = dia * 86400
    print('Hay un total de ',seg, 'en', dia,'dias.')

dia = ingreso_dias()
segundos_dias(dia)