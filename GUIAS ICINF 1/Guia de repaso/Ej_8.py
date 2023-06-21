"""Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estacion
correspondiente a ese mes: verano, otono, invierno o primavera."""

print("""      
      Escoje el número del mes y te diremos a la estación del año que corresponde:
                            ____________________
                            |                  |
                            | 1-     Enero     |
                            | 2-    Febrero    |
                            | 3-     Marzo     |
                            | 4-     Abril     |
                            | 5-     Mayo      |
                            | 6-     Junio     |
                            | 7-     Julio     |
                            | 8-     Agosto    |
                            | 9-   Septiembre  |
                            | 10-   Octubre    |
                            | 11-  Noviembre   |
                            | 12-  Diciembre   |
                            |__________________|
                            
                              Ejemplo: 1- Enero 
                     - Pertenece a la estación de verano. -     
      """)

while True:
    num = int(input("Elija el número de la estación correspondiente: "))
    if num <= 0 or num >= 13:
        print("Ingrese un numero valido")
    else:
        break
    
1.    
if num == 1:
    print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 1 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
    while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Enero está en la estación de Verano, puede ir a darse un descanso a la playa :)")
            break

2.
if num == 2:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 2 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 28 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 29:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Febrero está en la estación de Verano, puede ir a darse un descanso a la playa :)")
            break

3.
if num == 3:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 3 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        elif dia > 20 and dia < 32:
            print("              En esta fecha marzo está en la temporada de Otoño, abrigese que hará frio")
        else:
            print("         Marzo está en la estación de Verano, puede ir a darse un descanso a la playa :)")
            break
        break

4.
if num == 4:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 4 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 30 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 31:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Abril está en la estación de Otoño, abrigese que hará frio")
            break

5.
if num == 5:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 5 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Mayo está en la estación de Otoño, abrigese que hará frio")
            break

6.
if num == 6:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 6 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 30 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 31:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        elif dia > 20 and dia < 31:
            print("              En esta fecha Junio está en la temporada de Invierno, salga con paraguas que lloverá mucho")
        else:
            print("         Junio está en la estación de Invierno, salga con paraguas que lloverá mucho")
            break
        break

7.
if num == 7:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 7 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Julio está en la estación de Invierno, salga con paraguas que lloverá mucho")
            break

8.
if num == 8:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 8 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Agosto está en la estación de Invierno, salga con paraguas que lloverá mucho")
            break

9.
if num == 9:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 9 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 30 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 31:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        elif dia > 23 and dia < 31:
            print("              En esta fecha Septiembre está en la temporada de Primavera, una linda temporada para salir pasear")
        else:
            print("         Septiembre está en la estación de Invierno, salga con paraguas que lloverá mucho")
            break
        break

10.
if num == 10:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 10 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Octubre está en la estación de Primavera, una linda temporada para salir a pasear")
            break

11.
if num == 11:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 11 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 30 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 31:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        else:
            print("         Noviembre está en la estación de Primavera, una linda temporada para salir a pasear")
            break

12.
if num == 12:
     print("""
                           +-------------------------------------------+
                           |        USTED ELIGIO LA OPCION - 12 -       |
                           +-------------------------------------------+
                           |      El mes correspondiente contiene      |
                           |                 31 Días                   |
                           +-------------------------------------------+    
                           
                  Ahora indique la fecha del mes, para determinar en que temporada esta             
          """)
     while True:
        dia = int(input("                                                "))
        if dia < 1 or dia >= 32:
            print("          La fecha escrita no se encuentra dentro del mes, porfavor ingrese una fecha válida")
            continue
        elif dia > 21 and dia < 32:
            print("              En esta fecha Diciembre está en la temporada de Verano, y feliz navidad")
        else:
            print("         Diciembre está en la estación de Primavera, una linda temporada para salir a pasear")
            break
        break
