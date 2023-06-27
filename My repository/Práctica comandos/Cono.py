""" Construye un programa que, al recibir como datos el radio, la generatriz y la altura del cono, calcule e imprima el area de la base.
Datos: RAD, ALT GEN.
Donde RAD es una variable de tipo real que representa el radio del cono. ALT es una variable de tipo real que indica la altura

Consideraciones:

El area de la base se calcula asi:
area base = pi * radio^2

El area lateral se calcula asi:
area lateral = pi * radio * gene 

El area total se calcula como:
area total = ab + al 

El volumen se calcula de la siguiente forma:
Volumen = (1/3) * ab * altu """

pi = 3.14

def datos():
    radio  = float(input('ingrese el radio del cono: '))
    altura = float(input('ingrese la altura del cono: '))
    gene   = float(input('Ingrese la generatriz del cono: '))
    return radio,altura,gene

def calcular_area_base(radio):
    area_base = pi * radio ** 2
    print('El area base es: ',area_base)
    return area_base

def calcular_area_lateral(radio,gene):
    area_lateral = pi * radio * gene
    print('El area lateral es: ',area_lateral)
    return area_lateral

def calcular_area_total(area_base,area_lateral):
    area_total = area_base + area_lateral
    print('El area total es: ',area_total)
    return area_total

def calcular_volumen(area_base,altura):
    volumen = (area_base * altura) / 3
    print('El volumen del cono es: ',volumen)
    return volumen

radio,altura,gene = datos()
area_base         = calcular_area_base(radio)
area_lateral      = calcular_area_lateral(radio,gene)
area_total        = calcular_area_total(area_base,area_lateral)
volumen           = calcular_volumen(area_base,altura)
