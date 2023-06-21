"""Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de Programacion. Luego obtener el promedio ponderado de la
siguiente manera:
Promedio Ponderado = Lab1 * 0,3 + Lab2 * 0,4 + Lab3 * 0,3
Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprobo
la asignatura. Si el promedio es superior a 4,0, indicar que el estudiante aprobo
la asignatura. Si la nota es superior 6,0, debe mostrar el mensaje: el estudiante
aprobo con distincion"""

nota1 = float(input("Ingrese la nota 1 del laboratorio: "))
nota2 = float(input("Ingrese la segunda nota del laboratorio: "))
nota3 = float(input("Ingrese la ultima nota del laboratorio: "))

promedio = (nota1 * 0.3 + nota2 * 0.4 + nota3 * 0.3)
print("Tu promedio final es: ", round(promedio, 1))

if promedio < 4.0:
    print("Usted reprobo la asignatura")
elif promedio >= 4.0 and promedio <= 5.9:
    print("Usted aprobo la asignatura")
else:
    print("Usted aprobo la asignatura con distincion academica")
