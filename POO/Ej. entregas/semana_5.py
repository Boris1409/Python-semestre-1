
#calcular el área de un triángulo dados sus tres lados a, b, c.
#donde, corresponde al semiperímetro del triángulo


"""
Paso 1: Propósito completo
"""
# areaHeron: int int int->float
"""
Paso 2: Ilustrar ejemplo(s)
•No se codifica aún
"""
# Ejemplo #
#### areaHeron(2,3,5) entrega(0.0)
#### areaHeron(5,7,8) entrega(17.320)

"""
Paso 3: Codificar
"""
def areaHeron(a, b, c):
    
   
    # s = (a + b + c) / 2
    # area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    pass
    # return area

"""
Paso 4: Testing con assert
"""

assert areaHeron(13,14,15) == 84.0  ### Correcto
# assert areaHeron(13,14,15) == 0.1  ### Incorrecto


"""
Extra: Seccion de Prueba de la Funcion (Opcional)
"""

### Me dio curiosidad y me inspire 

# a = int(input("Ingrese el Valor del Lado a: "))
# b = int(input("Ingrese el Valor del Lado b: "))
# c = int(input("Ingrese el Valor del Lado c: "))
# resultado = areaHeron(a, b, c)
# print(f"El área del triángulo con lados {a}, {b}, {c} es {resultado}")

