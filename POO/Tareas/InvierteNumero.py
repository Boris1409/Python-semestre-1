"""
Defina una función invierteNumero, que
reciba un número entero positivo de tres dígitos
y entregue el número de entrada al revés. 

Importante: calcúlelo de forma algebraica sin
trabajar los dígitos como cadena de texto.
"""

def invierteNumero():
    while True:
        try:
            num = input('Ingrese un número que esté compuesto de 3 dígitos: ')
            if len(num) != 3 or not num.isdigit():
                print('El número debe tener exactamente 3 dígitos, intente nuevamente.')
                continue
            else:
                break
        except ValueError:
            print("""
                      
                      
                      |======================================|
                      |                                      |
                      |  ERROR, Ingrese nuevamente el número |
                      |                                      |
                      |======================================|
                      
                      
                      """)
    
    num = int(num)
    digito_1 = num // 100
    digito_2 = (num // 10) % 10
    digito_3 = num % 10
    
    num_invertido = digito_3 * 100 + digito_2 * 10 + digito_1
    
    return num_invertido

numero_invertido = invierteNumero()
print("Número invertido:", numero_invertido)
