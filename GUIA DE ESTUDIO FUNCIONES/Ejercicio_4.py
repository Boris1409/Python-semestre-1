'''Disenar un algoritmo que pueda actuar como un cajero, que devuelve y desglosa el vuelto 
en billetes y monedas (pesos chilenos). Utilizando funciones en Python.'''

def sueldo_total(sueldo):
    while True:
        if sueldo <= 0:
            print(' Lo sentimos, no se pueden realizar operaciones con ese monto.')
            sueldo = int(input(' Ingrese un monto valido '))
            continue
        else:
            print(' Muy bien sigamos ')
            break
    return sueldo
    
sueldo = int(input(' Ingrese su sueldo '))
sueldo_total = sueldo_total(sueldo)