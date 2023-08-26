""" - Defina una función farenheitACelsius,
que reciba de entrada una temperatura en
grados Farenheit y produzca de salida la
temperatura correspondiente en grados
Celsius. Busque la fórmula de conversión. -

Formula de Farenheit a Celsius: C = (F - 32) * (5/9)  

"""

def FarenheitACelsius():
    F = int(input('Ingrese la cantidad de grados Farenheit: '))
    formula = (F - 32) * (5/9)
    print(F,'grados Farenheit es equivalente a',round(formula),'Celsius')

FarenheitACelsius()
    
 