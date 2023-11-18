# CAMPOS:
# bencina: int

class Auto: 
    
    # CONSTRUCTOR: (Este metodo no hace return)
    # INSTAANCIA o crea un objeto de tipo Auto
    
    # recibe benc liros de bencina de un Auto
    def __init__(self,benc):
        
        self.bencina = benc
        print('Este auto tiene', self.bencina, 'litros de bencina en su estanque')
        
    def arrancar(self):
        if self.bencina > 0:
            print('Arrancamos')
        else:
            print('No podemos arrancar')
    def conducir(self):
        if self.bencina > 0:
            self.bencina -= 1
            return 'Quedan', self.bencina, 'litros'
        else:
            return 'No se mueve'
            
auto_mio = Auto(20)
auto_tuyo = Auto(15)
amigo_juan = Auto(5)

