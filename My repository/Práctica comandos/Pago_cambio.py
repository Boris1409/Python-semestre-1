""" Contruir un programa que, al recibir como datos el costo de un articulo vendido y la cantidad de dinero entregada calcule:
1. El cambio que se debe entregar al cliente, si el pago efectuado es mayor que el precio del produto.
2. ¿Qué pasa si el cliente paga exactamente lo que vale el producto?
3. La cantidad de dinero que falta por pagar, si el pago efectuado es menor que el precio del producto.
"""

print("""
        - Artículos -
    1. Monster      =   1800
    2. RedBull      =   1400
    3. Napolitana   =   2000
""")

Monster = 1800
RedBull = 1400
Napolitana = 2000 

def articulo():
    while True:
        n_compra = int(input('Elige el numero del articulo '))
        if n_compra < 1 or n_compra > 3:
            print('Pofavor, elija la opcion que este dentro de los articulos')
            continue
        else:
            break
    return n_compra

def opcion_1(n_compra):
    if n_compra == 1:
        while True:
            print("""
                  Su articulo cuesta:""",Monster
                  )
            monto = int(input('\nIngrese el dinero para pagar '))
            if monto < Monster:
                print('Dinero insuficiente, ingrese mas dinero')
                continue
            else:
                vuelto = monto - Monster
                print('Perfecto, su vuelto es de ', vuelto)
            break
        
def opcion_2(n_compra):
    if n_compra == 2:
        while True:
            print("""
                  Su articulo cuesta:""",Monster
                  )
            monto = int(input('\nIngrese el dinero para pagar '))
            if monto < RedBull:
                print('Dinero insuficiente, ingrese mas dinero')
                continue
            else:
                vuelto = monto - RedBull
                print('Perfecto, su vuelto es de ', vuelto)
            break

def opcion_3(n_compra):
    if n_compra == 3:
        while True:
            print("""
                  Su articulo cuesta:""",Monster
                  )
            monto = int(input('\nIngrese el dinero para pagar '))
            if monto < Napolitana:
                print('Dinero insuficiente, ingrese mas dinero')
                continue
            else:
                vuelto = monto - Napolitana
                print('Perfecto, su vuelto es de ', vuelto)
            break

n_compra = articulo()    
opcion_1(n_compra)
opcion_2(n_compra)
opcion_3(n_compra)