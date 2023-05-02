# Este es un ejemplo de uso class 
# Permiten definir objetos con propiedades y métodos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es " + self.nombre) 

persona = Persona("Juan", 25)
persona.saludar()
