""" En una casa de cambio necesitan construir un programa tal que al dar como dato una cantidad expresada en dolares, la convierta a pesos chilenos"""

def precio_dolar():
    pDolar = float(input('Ingrese el precio actual del dolar '))
    dolares = float(input('Ingrese la cantidad de dolares a convertir '))
    return dolares,pDolar

def convertidor(pDolar,dolares):
    cPesos = dolares * pDolar
    print(dolares, 'dolares, equivalen a ',cPesos, 'pesos')

pDolar,dolares = precio_dolar()
convertidor(pDolar,dolares)
