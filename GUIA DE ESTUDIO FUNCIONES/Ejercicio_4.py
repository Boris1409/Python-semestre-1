'''Disenar un algoritmo que pueda actuar como un cajero, que devuelve y desglosa el vuelto 
en billetes y monedas (pesos chilenos). Utilizando funciones en Python.'''

billetes=[20000,10000,5000,2000,1000]
monedas=[500,100,50,10]
valor_de_compra=25550
vuelto_desglosado={}
paga=int(input(f"""El valor de su compra corresponde a ${valor_de_compra}
¿Con cuanto paga?
con: $"""))
vuelto=paga-valor_de_compra
while True:
    if not paga%10==0:
        print("Valor invalido, recuerda que en Chile la moneda de menor valor es 10")
        paga=int(input("Ingrese un monto valido para realizar su compra: "))
    else:
        if paga<valor_de_compra:
            print(f"""Paga insufiiente.
            Faltan pagar: ${valor_de_compra-paga}
            """)
            sum_paga=int(input("Ingrese mas dinero: "))
            paga+=sum_paga
            # print(valor_de_compra-paga)
        elif paga>valor_de_compra:
            print(f"""¡Pago exitoso!
            Su vuelto es de: ${vuelto}
            """)
            if vuelto > 990:
                for i in billetes:
                    if vuelto // i > 0:
                        vuelto_desglosado[i] = vuelto // i
                        vuelto -= i * vuelto_desglosado[i]
            elif vuelto <= 990:
                for i in monedas:
                    if vuelto // i > 0:
                        vuelto_desglosado[i] = vuelto // i
                        vuelto -= i * vuelto_desglosado[i]
            for i,j in vuelto_desglosado.items():
                print(j,i)
                break
        else:
            print("""¡Pago exitoso!
            Su compra fue realizada con exito, no le corresponde vuelto, ya que pago con lo justo.""")
            break            
