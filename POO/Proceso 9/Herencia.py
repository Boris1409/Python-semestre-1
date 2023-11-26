import math
class Figura:
    def __init__(self,x) -> None:
        assert x>0
        self.x=x

class Circulo(Figura):
    def area(self):
        return math.pi*self.x**2
    def perimetro(self):
        return 2*math.pi*self.x
    
class Cuadrado(Figura):
    def perimetro(self):
        return 4*self.x
    def area(self):
        return self.x**2

class Rectangulo(Figura):
    def __init__(self, x,y) -> None:
        super().__init__(x)
        assert y>0
        self.y=y
    def area(self):
        return self.x*self.y
    def perimetro(self):
        return self.x*2+self.y*2
