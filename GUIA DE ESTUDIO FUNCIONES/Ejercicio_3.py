""". Crear un algoritmo que permita saber si un ano es bisiesto (calendario gregoriano) desde el año 0 en adelante. Utilizar funciones para resolver el problema."""

def año_bisiesto(año):
    while True:
        if año <= 0:
            año = int(input("Porfavor, indique un año válido: "))
            continue
        else:
            break
    if año <= 1582:
        print("|",año,"| ","No está dentro del período del calendario gregoriano")
    else:
        if año % 4 != 0:
            print("|",año,"| ","Es un año común")
        elif año % 100 != 0:
            print("|",año,"| ","Es un año bisiesto")
        elif año % 400 != 0:
            print("|",año,"| ","Es un año común")
        else:
            print("|",año,"| ","Es un año bisiesto")
    return ''
        

año = int(input("\nIngrese el año: "))
comprobacion = año_bisiesto(año)
print(comprobacion)
