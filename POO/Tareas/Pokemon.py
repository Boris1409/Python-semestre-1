#  EL CODIGO SE DEFINE PORLA CLASE LLAMADA POKEMON
class Pokemon:
    
    # CON EL METODO CONSTRUCTOR __init__ SE USA PARA INICIALIZAR LOS ATRIBUTOS DEL OBJETO POKEMON 
    def __init__(self, nombre, tipo, altura, peso, sexo):
        self.nombre  = nombre
        self.tipo = tipo
        self.altura = altura
        self.peso = peso
        self.sexo = sexo
    
    # METODOS PARA ESTABLECER ESTADISTICAS DEL POKEMON 
    def setPS_base(self, ps_base):
        self.ps_base = ps_base
    
    def setAtaque(self, ataque):
        self.ataque = ataque
        
    def setDefensa(self, defensa):
        self.defensa = defensa
        
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
        
    
    # METODO PARA MOSTRAR LOS ATRIBUTOS DEL POKEMON DE UNA MANERA ESTRUCTURADA
    def MostrarAtributos(self):
        print(f"""
              - Nombre: {self.nombre}
              - Tipo: {self.tipo}
              - Altura: {self.altura}m
              - Peso: {self.peso}kg
              - Sexo: {self.sexo}
              - PS_Base: {self.ps_base}
              - Ataque: {self.ataque}
              - Defensa: {self.defensa}
              - Velocidad: {self.velocidad} 
              """)
    
    # METODO PARA COMPARAR LAS ESTADISTICAS DE DOS POKEMON Y DEVUELVE UN TRUE SI EL PRIMER POKEMON
    # TIENE ESTADISTICAS PROMEDIOS MAYORES QUE EL SEGUNDO POKEMON Y FALSE DEL CASO CONTRARIO
    def EsMejorQue(self, pokemon_2 ):
        return ((self.ps_base + self.ataque + self.defensa + self.velocidad)/4 > (pokemon_2.ps_base + pokemon_2.ataque + pokemon_2.defensa + pokemon_2.velocidad)/4)

# SE CREAN DOS INSTANCIAS DE POKEMON Y SON LLAMADAS A METODOS 
1.
pika = Pokemon("Pikachu", "Eléctrico", 0.4, 6.0, "H")
pika.setPS_base(3)
pika.setAtaque(13)
pika.setDefensa(10)
pika.setVelocidad(15)

2.
charma = Pokemon("Charmander", "Fuego", 0.6, 8.5, "M")
charma.setPS_base(3)
charma.setAtaque(4)
charma.setDefensa(3)
charma.setVelocidad(4)

# MOSTRAMOS LOS ATRIBUTOS DE AMBOS POKEMON
pika.MostrarAtributos()
charma.MostrarAtributos()

# SE LLAMA AL METODO PARA COMPARAR SUS ESTADISTICAS Y MOSTRAR EL RESULTADO 
print(pika.EsMejorQue(charma))  