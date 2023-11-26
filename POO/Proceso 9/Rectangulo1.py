from Rectangulo import Rectangulo

# clase: Rectangulo1 
# herencia: Rectangulo 
class Rectangulo1(Rectangulo):
    
    # constructor: int, int -> Rectangulo1
    # Forma Rectangulo1 tomando en cuenta su ancho x y su altura y
    # Ejemplo: r1 = Rectangulo1(4,5)
    def __init__(self, x, y):
        Rectangulo.__init__(self, x, y)

    # rotar: None -> None
    # Intercambia los valores de ancho a alto, y de alto a ancho
    # Ejemplo: r1, ancho = 4, alto = 9 
    # r1.rotar(), el nuevo ancho seria 9, y el nuevo alto seria 4
    def rotar(self):
        ancho =self.ancho
        alto = self.alto
        self.ancho = alto
        self:alto = ancho

    # pintar: str -> None  
    # Muestra en la pantalla un rectangulo que si es rellenado por c = "*"
    # Ejemplo: r1.pintar(c), muestra en pantalla un rectangulo de 4x3 rellenado por c = "*"
    def pintar(self, c):
        for i in range(self.alto):
            for j in range(self.ancho):
                print(c, end="")
            print()


mix_rectangulos = []
while True:

    ancho = int(input("Indique el ancho "))
    alto = int(input("Indique el alto "))

    if ancho == 0 and alto == 0:
        break

    r = Rectangulo1(ancho, alto)
    mix_rectangulos.append(r)

    print()
    r.dibujar('*')
    print('')

rectangulo_mas_grande = max(mix_rectangulos)
print("\nMas grande rotado:\n")
rectangulo_mas_grande.rotar()
rectangulo_mas_grande.pintar('*')
