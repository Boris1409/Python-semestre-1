# clase: Rectangulo
# atrbutos: x, y = int
class Rectangulo:

    # Constructor: int, int -> Rectangulo
    # Forma un rectangulo tomando en cuenta su valor de ancho que es x y su altura que es y
    # Ejemplo: r1 = Rectagulo(5,4)
    def __init__(self, x, y):
        self.ancho = x
        self.alto = y

    # __gt__: Rectangulo bool o 0
    #  La funcion devuelve True si el area de r1 es mayor que r2.
    #  Devuelve False en caso contrario.
    # Y devuelve 0 en caso de que el area de r1 es igual a r2
    # Ejemplo: r1, ancho=5, alto=6. Y r2, ancho=3, alto=2
    # r1.__gt__(r2) entrega True
    def __gt__(self, x):
        area_1 = (self.ancho * self.alto) 
        area_2 = x.ancho * x.alto
        
        if area_1 > area_2:
            return True
        elif area_1 < area_2:
            return False
        else:
            return 0
    
    # dibujar: str -> None
    # Lo que se ve printeado en pantalla es c="*", conocido como el borde de la figura.
    # Ejemplo: r1.dibujar(c), imprime los bordes del rectangulo x*y usando "*"
    def dibujar(self, c):
        fila = 0
        if self.alto>=2:
            print("")
            print(f"{self.ancho*c}")
            while fila < self.alto-2:
                fila += 1
                print(c+(" "*(self.ancho-2))+c)
            print(f"{self.ancho*c}")
            print("")
        else:
            print("")
            print(f"{self.ancho*c}")
            while fila <self.alto-2:
                fila += 1
                print(c+(" "*(self.ancho-2))+c)
            print("") 
    
