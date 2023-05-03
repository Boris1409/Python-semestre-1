"""03-Operadores"""

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

bencina = True
encendido = True
edad = 19

1. #If and
if bencina and encendido:  #El "and" tienen que cumplirse ambas condiciones
    print("El vehiculo puede avanzar","\n")
else:
    print("El vehiculo no puede arrancar","\n")

2. #If or
if bencina  or encendido: #El "or" basta con que se cumpla una condicion 
    print("El vehiculo puede correr,","\n")
else:
    print("El vehiculo no puede arrancar","\n")
    
3. #If not, and
if not bencina and encendido: #El "not" es una contradiccion, si es true = false y si es false = true 
    print("")
else:
    print("El vehiculo no puede arrancar","\n")
    
4. #If not, and
if not bencina or (encendido and edad >= 99):
    print("Esta maquina correra","\n")
else: 
    print("Este tarro ni se movera","\n")
    