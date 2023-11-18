####Codifique la función areaHeron para calcular el área de un triángulo dados sus tres lados a, b, c

#### Definir una funcion que calcule el area de un triangulo ocupando la formula de Heron

### AreaHeron num -> float (Float ya que puede haber decimales)

## Descripción: Dar datos del triangulo para calcular su area

import math

def AreaHeron (a,b,c):

    s= (a+b+c)/2 ##Los valores seran 6, 8 y 10 = 12
    
    A= s * (s-a) * (s-b) * (s-c) 

    AREA = math.sqrt(A) 

    return AREA

print(AreaHeron(6,8,10))
