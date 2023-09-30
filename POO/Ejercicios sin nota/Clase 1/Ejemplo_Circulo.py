""" -Problematica calcular el area del circulo - """

r  = 1
formula_area = 3.14 * r ** 2
print(formula_area)    

""" - Trabajando con funciones - """

def area_circulo(radio):
    pi = 3.14
    formula = pi * radio ** 2
    return formula

print(area_circulo(5))

""" - Trabajando con el radio de un anillo - """

def areaAnillo(radioExt, radioInt):
    return area_circulo(radioExt) - area_circulo(radioInt)

print(areaAnillo(5,1))