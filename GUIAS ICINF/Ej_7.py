"""Crear una lista con nombres de 5 trabajadores y otra lista con las edades de
estos 5 trabajadores, Se solicita relacionar ambas listas en una sola estructura.
La salida puede ser en tuplas o en un diccionario."""

nombres = ("Boris", "Matias", "Cristian", "Diego", "Franco")
edades = (18, 29, 18, 18, 17,)

registros = dict(zip(nombres, edades))
print(registros)