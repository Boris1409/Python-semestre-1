"--------------------------------------- IMPLEMENTACION ParDeNumeros (1) ----------------------------------"

# Campos: 
# limite : int
# valor : int

class ParDeNumeros:
    # Constructor: Crea un objeto que almacena dos numeros y se reinicia a cero cuando pase el limite.
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0
        
    # getValor : None -> int
    # Retorna el valor actual 
    def getValor(self):
        return self.valor
    
    "------------------------------------ IMPLEMENTACION ParDeNumeros (2) ---------------------------------------" 
    
    # setValor : int -> None 
    # efecto : Reemplaza  el valor del par por nuevo valor
    def setValor(self, nuevoValor):
        if (nuevoValor >= 0) and (nuevoValor < self.limite):
            self.valor = nuevoValor
            
        # toString : -> str 
        # Retorna el valor almacenado en un string que contiene los numeros del par; si el valor es menor que diez, se le debe anteponer un cero 
    def toString(self):
            if self.valor < 10:
                return  "0" + str (self.valor)
            else:
                return str(self.valor)
    "------------------------------------- IMPLEMENTACION ParDeNumeros (3) --------------------------------------"
    
    # aumentar : None -> None
    # efecto : Aumenta  en una unidad el valor almacenado en el par, reiniciando a cero si se sobrepasa el limite 
    def aumentar(self):
        self.valor = (self.valor +1) % self.limite 
        
    "------------------------------------- IMPLEMENTACION DE Reloj (1) -----------------------------------------"
    
    # aumentar : None -> None 
    # campos : 
    # horas : ParDeNumeros 
    # minutos : ParDeNumeros 
    # pantalla : str 
class Reloj:
    # Constructor : crea un objeto reloj.
    # Si no recibe parametros, inicia el reloj a las 00:00; si recibe, a la hora indicada 
    def __init__(self, horas = 0, minutos = 0):
        self.horas = ParDeNumeros(24)
        self.minutos = ParDeNumeros (60)
        self.setReloj(horas, minutos)
    
    "------------------------------------- IMPLEMENTACION DE Reloj (2) -----------------------------------------"
    
    # tic : None -> 
    # Se llama cada minuto, hace avanzar el reloj un minuto
    def tic(self):
        self.minutos.aumentar()
        if self.minutos.getValor() == 0:
            self.horas.aumentar()
        self.actualizarPantalla()
            
    # setReloj : int int -> None
    # efecto : Fija la hora y minuto a los especificados
    def setReloj(self, hora, minuto):
        self.horas.setValor(hora)
        self.minutos.setValor(minuto)
        self.actualizarPantalla()
            
    "-------------------------------------- IMPLEMENTACION DE Reloj (3) -----------------------------------------"
    
    # tic : None -> None 
    def getHora(self):
        return self.pantalla
    
    # actualiazar : None -> None 
    # efecto Actualiza el string interno que lleva cuenta de la hora actual 
    def actualizarPantalla(self):
        self.pantalla = self.horas.toString() + ":" + self.minutos.toString()
        
    "--------------------------------------- TESTING PARA ParDeNumeros ------------------------------------------"
    
    # Para simplificar la implementacion de los tests, este codigo se incluye en el archivo donde se encuentra la definicion de la clase ParDeNumeros
class TestParDeNumeros:
    def __init__(self):
        # crear un objeto con estado interesante
        self.par = ParDeNumeros(3)
        
    def test(self):
        # ejercitar funcionalidad, y verifcar sju comportamiento
        assert self.par.getValor() == 0
        self.par.aumentar()
            
        assert self.par.getValor() == 1
        self.par.aumentar()
            
        assert self.par.getValor() == 2
        self.par.aumentar()
            
        assert self.par.getValor() == 0
        self.par.aumentar()
            
        assert self.par.toString() == "01"
            
# Ejecucion del test
test = TestParDeNumeros()
test.test()

"----------------------------- TESTING PARA Reloj -------------------------------"

class TestReloj:
    
    def __init__(self):
        # crear un objeto con estado interesante
        self.reloj = Reloj(23, 58)
        
    def test(self):
        # ejercitar funcionalidad y verificar su comportamiento 
        assert self.reloj.getHora() =="23:58"
        self.reloj.tic()
        
        assert self.reloj.getHora() == "23:59"
        self.reloj.tic()
        
        assert self.reloj.getHora() == "00:00"
        for i in range(60):
            self.reloj.tic()
        
        assert self.reloj.getHora() == "01:00"
        self.reloj.tic()
        
        assert self.reloj.getHora() == "01:01"
        

test = TestReloj()
test.test()