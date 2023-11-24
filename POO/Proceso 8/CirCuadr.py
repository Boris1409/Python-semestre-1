import Cuadrado
import Circulo
# import math




r = input("Ciruco o cuadrado? ").lower()

if r == "circulo":
    c = Circulo(input("radio? "))
elif r == "cuadrado":
    c = Cuadrado(input("lado? "))
else:
    print("Debe ser Circulo o cuadrado")

if c!= None:
    print("area =",c.area())
    print("perimetro =",c.perimetro())