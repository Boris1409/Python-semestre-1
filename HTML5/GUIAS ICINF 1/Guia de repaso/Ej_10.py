"""Crear una agenda telefonica que contenga un solo contacto. Esta agenda se debe
guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
Nombre
Direccion
Ciudad
Numero telefonico
A continuacion, agrega una nueva clave llamada “Redes Sociales” que contenga al
menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
Instagram y Twitter). Por ultimo, se solicita imprimir solamente el Facebook del
contacto y luego la agenda completa actualizada."""

agenda = {
    "Nombre": "Boris",
    "Direccion":"Juan Queipul",
    "Ciudad":"La Union",
    "Numero telefonico":"9 91199122"
}
agenda.add("Redes Sociales")
print(agenda)