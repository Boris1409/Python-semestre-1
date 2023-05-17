""". Existen dos grupos de estudiantes de la carrera de Programacion que formaron
sus grupos para elaborar el Laboratorio N°3. Los grupos son los siguientes:

Grupo 1
Marcos
Gabriela
Benjamin
Matias

Grupo 2
Marcos
Nicolas
Diego
Matias

Se necesita saber si en ambos grupos tienen algun estudiante en comun y, en caso
de que asi sea, imprimir los nombres de esos estudiantes. Todo esto utilizando
Sets.
"""

grupo1 = {"Marcos","Gabriela","Benjamin","Matias"}
grupo2 = {"Marcos", "Nicolas", "Diego", "Matias"}
rep = grupo1 & grupo2

if len(rep) == 0:
    print("No hay estudiantes que se repitan")
else:
    print("Los estudiantes en que se repiten son:")
    for estudiante in rep:
        print(estudiante)