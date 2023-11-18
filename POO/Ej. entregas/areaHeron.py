#areaHeron: decimal o entero ---> decimal
#recibe el valor de tres lados de un triangulo 
#areaHeron(lado1,lado2,lado3), entrega el area del triangulo calculado con la formula de heron 

import math

def areaHeron(a,b,c):
    #Se comprueba que los lados ingresados pertenescan a un triangulo verdadero
    if a+b <= c or a+c <= b or b+c <= a:
        return('Los lados ingresados no pertenecen a un triangulo verdadero')
    else:    
        #se saca el area con la formula de heron
        s = (a + b + c) / 2 
        A = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return f'el area del triangulo es {round(a,2)}'

lado_1 = float(input('Ingrese primer lado del triangulo: '))
lado_2 = float(input('Ingrese segundo lado del triangulo: '))
lado_3 = float(input('Ingrese tercer lado del triangulo: '))

print(areaHeron(lado_1,lado_2,lado_3))