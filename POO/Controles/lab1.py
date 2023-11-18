# litros: num num -> num 
# Calcular la distancia de bencina en funcion de la distancia recorrida y el rendimiento del vehiculo, donde uno de sus lados es dRecorrida y el otro rendimiento.
# def litros(dRecorrida, rendimiento):
# ...
# ejemplo: litros(40,15):
# entrega 2.6666666666666665


def litros(dRecorrida, rendimiento): 
    # Se calcula la cantidad de bencina que se usara tomando en cueta la distacia y el rendimiento, sabemos que el rendimiento del vehiculo son 15km/l, donde 1 litro sirve para recorrer 15km.
    #Entonces la operación consta en dividir la dRecorrida por el rendimiento del vehiculo.
    return dRecorrida / rendimiento

assert litros(40,15) == 2.6666666666666665


# costo_bencina: num num -> num
# Calcular el costo de bencina en funcion de su precio y litros llenados al estanque, donde uno de sus datos es precio y el otro  litros
# def costo_bencina(precio, litros):
# ... 
# ejemplo: costo_bencina(1097,2.6):
# entrega 2852.2000000000003

def costo_bencina(precio,litros):
    return precio * litros

assert costo_bencina(1097, 2.6) == 2852.2000000000003

