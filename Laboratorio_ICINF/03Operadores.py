bencina = True
encendido = True
edad = 19

if bencina and encendido: #El and tienen que cumplirse ambas condiciones
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    
if bencina  or encendido: #El or basta con que se cumpla una condicion 
    print("El vehiculo puede correr")
else:
    print("El vehiculo no puede arrancar")
    

if not bencina and encendido: #El not es una contradiccion, si es true = false y si es false = true 
    print("")
else:
    print("El vehiculo no puede arrancar")
    
if not bencina or (encendido and edad >= 99):
    print("Esta maquina correra")
else: 
    print("Este tarro ni se movera")
    