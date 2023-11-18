
def cal(diasXMes, nombreMes, diaSemana):
    # Primero se tiene que determinar si el año es bisiesto o no
    es_bisiesto = diasXMes[1] == 29

    # Usamos el recorrido for para generar el calendario de cada mes y la funcion enumerate() para saber el valor de su elemento como su posicion con el iterador 
    for mes, nombre_del_mes in enumerate(nombreMes):
        print(nombre_del_mes)
        print("Mo Tu We Th Fr Sa Su")

        # Se calcula el numero de dias para el mes que correspond
        dias_del_mes_actual = diasXMes[mes]

        # Si el año es bisiesto entonces el mes de febrero se acopla a 29 dias
        if mes == 1 and es_bisiesto:
            dias_del_mes_actual = 29

        # Se determina la posicion de la fecha de la primera semana del mes, para que sea continuo y no haya dos dias en uno
        posicion_inicial = (diaSemana - 1) % 7

        # Finalmente se imprime cantidad de dias del mes en el calendario
        for j in range(posicion_inicial):
            print("  ", end=" ")
            
        for dia in range(1, dias_del_mes_actual + 1):
            print(f"{dia:2d} ", end="")
            posicion_inicial += 1
            if posicion_inicial % 7 == 0:
                print()

        # Se imprime un salto de linea al final del mes para que se vea mas ordenado
        print("\n")

        # Calula el dia que empezara la primera semana en el siguiente mes 
        diaSemana = (diaSemana + dias_del_mes_actual) % 7 + 0

# Se establece la cantidad de dias por mes y sus respectivos nombres de cada uno
diasXMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nombreMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
diaSemana = 1

# Por ultimo se llama a la funcion cal() para mostrar el resultado
# La razon por la que no aparece el diaXSemana es porque en su lugar se determinara el dia en que iniciaria el año, ej: 2 -> entonces el año empezara el dia martes y seguira su curso respetando el orden
cal(diasXMes, nombreMes, diaSemana)