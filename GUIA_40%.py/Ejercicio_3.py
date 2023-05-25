"""Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada 
uno). Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo
con los siguientes puntos:

a) La tarifa de las horas diurnas es de 12000 CLP.
b) La tarifa de las horas nocturnas es de 16000 CLP.
c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el
turno nocturno.

Ademas considerar: 

a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves 
y Viernes en turnos diurnos.
b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tam- 
bien el de dia domingo en turno diurno.
c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, Sabado y Domingo 
en turnos nocturnos.

Guardar la informacion de cada empleado en un diccionario, con el pago diario que debe 
recibir cada empleado y el total de la semana.
"""
turno_diurno = 12000*10
turno_nocturno = 16000*10
dom_diurno = (12000+2000)*10
dom_nocturno = (16000+3000)*10  

empleados = {
    1: {
        "Nombre" : "Boris",
        "Lunes" : turno_nocturno,
        "Martes" : turno_nocturno,
        "Miercoles" : turno_nocturno,
        "Jueves" : turno_diurno,
        "Viernes" : turno_diurno
        },
    
    2: {
        "Nombre" : "Franco",
        "Martes" : turno_nocturno,
        "Miercoles" : turno_nocturno,
        "Jueves" : turno_nocturno,
        "Domingo" : dom_diurno
        },
    
    3: {
        "Nombre" : "Cristian",
        "Miercoles" : turno_diurno,
        "Jueves" : turno_diurno,
        "Viernes" : turno_diurno,
        "Sabado" : turno_nocturno,
        "Domingo" : dom_nocturno
    }
}

print("""\n -EMPLEADOS- """,
      "\n1:", 
        "\nNombre :Boris",
        "\nLunes :", turno_nocturno,
        "\nMartes :", turno_nocturno,
        "\nMiercoles :", turno_nocturno,
        "\nJueves :", turno_diurno,
        "\nViernes :", turno_diurno,
        
        "\n2:", 
        "\nNombre : Franco""",
        "\nMartes :", turno_nocturno,
        "\nMiercoles :", turno_nocturno,
        "\nJueves :", turno_nocturno,
        "\nDomingo :", dom_diurno,
        
        "\n3:",
        "\nNombre : Cristian",
        "\nMiercoles :", turno_diurno,
        "\nJueves :", turno_diurno,
        "\nViernes :", turno_diurno,
        "\nSabado :", turno_nocturno,
        "\nDomingo :", dom_nocturno,
        )

print("\nEmpleado 1:")
print("El pago diario nocturno del 1er empleado es:",turno_nocturno,'CLP',"\nEl pago diario diurno del 1er empleado es:",turno_diurno,'CLP',"\nEl pago semanal del 1er empleado es:",(turno_nocturno*3+turno_diurno*2),'CLP')

print("\nEmpleado 2:")
print("El pago diario nocturno del 2do empleado es:",turno_nocturno,'CLP',"\nEl pago diario diurno del 2do empleado es:",dom_diurno,'CLP',"\nEl pago semanal del 2do empleado es:",(turno_nocturno*3+dom_diurno),'CLP')

print("\nEmpleado 3:")
print("El pago diario nocturno del 3er empleado es:",turno_nocturno+dom_nocturno,'CLP',"\nEl pago diario diurno del 3er empleado es:",turno_diurno,'CLP',"\nEl pago semanal del 3er empleado es:",(turno_nocturno+dom_nocturno+turno_diurno*3),'CLP')

empleados[1]["Pago diario Lunes, Martes y Miercoles"] = (turno_nocturno )
empleados[1]["Pago diario Jueves y Viernes"] = (turno_diurno)
empleados[1]["Pago semanal"] = (turno_nocturno*3 + turno_diurno*2)

empleados[2]["Pago diario Martes, Miercoles y Jueves"] = (turno_nocturno)
empleados[2]["Pago diario Domingo"] = (dom_diurno)
empleados[2]["Pago semanal"] = (turno_nocturno*3 + dom_diurno)


empleados[3]["Pago diario Miercoles, Jueves y  Viernes"] = (turno_diurno)
empleados[3]["Pago diario Sabado y Domingo"] = (turno_diurno, turno_nocturno)
empleados[3]["Pago semanal"] = (turno_nocturno + turno_diurno*3 + dom_nocturno)

for i, j in empleados.items():
    print('\n',i, ':', j)