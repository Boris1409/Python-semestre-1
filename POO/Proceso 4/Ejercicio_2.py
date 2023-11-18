# asistentes: num -> float
# Calcular la cantidad de asistentes segun el precio de la entrada, donde pe es el precio de la entrada
# ejemplo: asistentes(4000) -> 120
def asistentes(pe):
    return(-3 / 100) * pe + 240

assert asistentes(4000) == 120

# ingresos: num -> float
# Calcular el ingreso total del dinero, en funcion del precio de la entrada y de los asistnetes
# ejemplo: ingresos(4000) -> 480000.0
def ingresos(pe):
    return pe * asistentes(pe)

assert ingresos(4000) == 480000.0

# costoTotal: num -> num
# calcular los costos, segun el precio de la entrada
# ejemplo: costoTotal(4000) -> 163600.0
def costoTotal(pe):
    return 160000 + 30 * asistentes(pe)

assert costoTotal(4000) == 163600.0

# beneficios: num -> num
# calcular el beneficio segun los ingresos y el costo total, en funcion del precio de la entrada
# ejemplo: beneficios(4000) -> 316400.0
def beneficios(pe):
    return ingresos(pe) - costoTotal(pe)

assert beneficios(4000) == 316400.0

print(beneficios(4000))