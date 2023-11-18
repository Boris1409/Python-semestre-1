# se calcula el area de un triangulo con sus 3 lados

from math import sqrt

def areaHeron(a,b,c):
    semiperimetro= (a+b+c)/2
    area=  sqrt(semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c))
    print (f"El area del triangulo es: {round(area,1)}")

areaHeron(2,3,4)