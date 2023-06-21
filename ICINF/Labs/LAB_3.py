regiones = {
    14: {
        "Nombre": "Los Ríos",
        "Superficie": 18429,
        "Habitantes": 404432
    },
    12: {
        "Nombre": "Magallanes",
        "Superficie": 1382291,
        "Habitantes": 166533
    }
}
print(regiones)

# Crear una nueva clave al diccionario llamada “Densidad”. La densidad poblacional se
# calcula de la siguiente forma: (Densidad = Habitantes/Superficie). Solamente debe
# tener 1 decimal la salida del resultado.
for region in regiones.values():
    habitantes = region["Habitantes"]
    superficie = region["Superficie"]
    densidad = round(habitantes/superficie,1)
    region["Densidad"] = densidad
print(regiones)

# Agregar otra clave llamada “Capital”, correspondiente a la capital de cada región

regiones[14]["CAPITAL"] = "Valdivia"
regiones[12]["CAPITAL"] = "Punta. Arenas"
print(regiones)

# Agregar otra clave con el nombre “Comunas” la cual será una lista de 3 comunas de
# cada región como mínimo.

regiones[14]["COMUNAS"] = ["La Union", "Paillaco", "Rio Bueno"]
regiones[12]["COMUNAS"] = ["Tierra del Fuego","Última Esperanza","Antártica Chilena"]
print(regiones)

# Crear una última clave llamada “Provincia” la cual almacenará el nombres de las
# provincias correspondiente a cada región. Las provincias se guardarán en tuplas.

regiones[14]["PROVINCIA"] = ("Ranco", "Valdivia")
regiones[12]["PROVINCIA"] = ("Tierra del Fuego","Última Esperanza",)
print(regiones)

print(""" ESTE ES EL NUEVO DICCIONARIO""")

# regiones = {
#     14: {
#         "Nombre": "Los Ríos",
#         "Superficie": 18429,
#         "Habitantes": 404432,
#         "DENSIDAD": 21.9,
#         "CAPITAL": "Valdivia",
#         "COMUNAS": ["La Unión","Río Bueno", "Paillaco"],
#         "PROVINCIA": ("Ranco", "Valdivia")
#     },
#     12: {
#         "Nombre": "Magallanes",
#         "Superficie": 1382291,
#         "Habitantes": 166533,
#         "DENSIDAD": 0.1,
#         "CAPITAL": "Punta Arenas",
#         "COMUNAS": ["Magallanes", "Tierra del Fuego","Antártica Chilena"],
#         "PROVINCIA": ("Tierra del Fuego","Última Esperanza",)
#     }
# }

print(regiones)