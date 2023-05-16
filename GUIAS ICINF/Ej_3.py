"""Desarrollar un programa que al momento de ingresar los lados de un triangulo
(a, b y c) en consola, indique si es equilatero, isosceles o escaleno. Tambien se
solicita calcular el area utilizando la formula de Heron:
A
2 = p(p - a)(p - b)(p - c), donde p = a + b + c // 2"""

import math

a = float(input("Ingrese el lado a del triangulo: "))
b = float(input("Ingrese el lado b del triangulo: "))
c = float(input("Ingrese el lado c del triangulo: "))

if a == b and a == c and b == c:
    print("\nEs un triangulo equilatero")
elif a == b or a == c or b == c:
    print("\nEs un triangulo isósceles")
else:
    print("\nEs un triangulo escaleno")
    
lados = [a, b, c]
p = sum(lados)
sp = (p/2)
area = (sp*(sp - a)*(sp - b)*(sp - c))**0.5

print("\nEl perimetro del triangulo es: ",(p))
print("El area del triangulo es: ",round(area, 2))

# if per % 2 != 0:
#     res1 = print("El semiperimetro del triangulo es: ",round(sper, 1))
# else:
#     res2 = print("El SemiPerimetro del triangulo es : ",round(sem, 1))
#     if per % 2 == 0:
#         res1 = print("El semiperimetro del triangulo es: ",round(sper, 1))
#     else:
#         res2 = print("El SemiPerimetro del triangulo es : ",round(sem, 1))

# if res1 == sper:
#    print("El area del triangulo es: ",round(area, 1))
# else: 
#    print("El área del triangulo es: ",round(area2, 1))
#    if res2 == sper:
#        print("El area del triangulo es: ",round(area, 1))
#    else: 
#        print("El área del triangulo es: ",round(area2, 1))
#        if res1 == sem:
#            print("El area del triangulo es: ",round(area, 1))
#        else: 
#            print("El área del triangulo es: ",round(area2, 1))
        
        
        


