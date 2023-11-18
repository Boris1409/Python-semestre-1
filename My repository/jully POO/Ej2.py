# asistentes: num -> num
# calcula la cantidad de asistentes segun el precio de la entrada, donde pEntrada es el precio de la entrada
# ej: asistentes(4000) -> 120
def asistentes(pEntrada):
    return(-3 / 100) * pEntrada + 240
assert asistentes(4000) == 120

# ingreso: num -> float
# calcula el ingreso total del dinero, en funcion del precio de la entrada y de los asistnetes
# ej: ingresos(4000) -> 480000.0
def ingreso(pEntrada):
    return pEntrada * asistentes(pEntrada)
assert ingreso(4000) == 480000.0

# costoTotal: num -> num
# calcula los costos, segun el precio de la entrada
# ej: costoTotal(4000) -> 163600.0
def costoTotal(pEntrada):
    return 160000 + 30 * asistentes(pEntrada)
assert costoTotal(4000) == 163600.0

# beneficio: num -> num
# calcula el beneficio segun los ingresos y el costo total, en funcion del precio de la entrada
# ej: beneficio(4000) -> 316400.0
def beneficio(pEntrada):
    return ingreso(pEntrada) - costoTotal(pEntrada)
assert beneficio(4000) == 316400.0

print(beneficio(4000))