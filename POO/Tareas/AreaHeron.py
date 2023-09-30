# Primero se crea la funcion

def areaHeron(a,b,c):  
    # Para calcular el semiperimetro, sumamos todos sus lados y lo divimos por 2, usando la formula de Herón calcularemos su area
    s = (a + b +c) // 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    # El resultado será mostrado en patalla con un redondeo de dos decimales
    print(round(area,2))

areaHeron(13,14,15)