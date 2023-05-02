datos = {}

nombre = input("-Ingrese el nombre del estudiante: ")
asignatura = input("-Ingrese el nombre de la asignatura: ")
nota_laboratorio1 = float(input("-Ingrese la nota del laboratorio N1: "))
nota_laboratorio2 = float(input("-Ingrese la nota del laboratorio N2: "))

prom_pond = (nota_laboratorio1 * 0.3) + (nota_laboratorio2 *0.7)

datos["--Nombre del estudiante--"] = nombre
datos["--Nombre de la asignatura--"] = asignatura
datos["--Nota del Laboratorio Número 1--"] = nota_laboratorio1
datos["--Nota del Laboratorio Número 2--"] = nota_laboratorio2
datos["--Promedio final ponderado--"] = round(prom_pond, 1)

print("\n")

datos = {
    "nombre_estudiante": nombre,"\n"
    "nombre_asignatura": asignatura,
    "nota_1": nota_laboratorio1,
    "nota_2": nota_laboratorio2,
    "promedio": round(prom_pond,1)
}
print(datos)


