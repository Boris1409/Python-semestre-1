"""
Defina una función areaTriangulo, que
consuma un lado y la altura perpendicular a
este y entregue como salida el área del
triángulo. Busque la fórmula para calcularla.
"""

def areaTriangulo():
    base = int(input('Ingrese la base del Triangulo: '))
    altura = int(input('Ingrese la altura del Triangulo: '))
    area = (base * altura) / 2
    
    print('El area del triangulo es:',round(area))
    
areaTriangulo()