# beneficios : numero -> numero
# Calcula el beneficio como la diferencia entre
# ingresos y costos para un valor de entrada dado.
def beneficios(valorEntrada):
 return ingresos(valorEntrada) - costos(valorEntrada)

# ingresos : numero -> numero
# Calcula el ingreso total, dado el valor de la
# entrada.
def ingresos(valorEntrada):
 return valorEntrada * asistentes(valorEntrada)

# costos : numero -> numero
# Calcula los costos dado el valor de la entrada.
def costos(valorEntrada):
 return 160000 + 30 * asistentes(valorEntrada)

# asistentes : numero -> numero
# Calcula la cantidad asistentes dado el valor
# de la entrada.
def asistentes(valorEntrada):
 return 120 + 15 / 500 * (4000 - valorEntrada)