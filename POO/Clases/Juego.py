"--------------------------- Clase Juego 1 --------------------------------"

class Juego:
    # ... Codigo omitido...
    def crearEsceneas(self):
        afuera = Escena("Afuera de la entrada principal de la universidad")
        auditorio = Escena("Sala de conferencias")
        pub = Escena("En el pub del campus")
        lab = Escena("En un labotario de computacion")
        oficina = Escena("En la oficina principal de computacion")
        
    # Inicializar las salidas de la escena 
        afuera.self.salidas(None, auditorio, lab, pub)
        auditorio.setSaliddas(None, None, None, afuera)
        pub.setSalidas(afuera, oficina, None, None)
        self.escenaActual = afuera
    
    "----------------------- Clase Juego 2 ---------------------------------------"
    # Imprime en pantalla el mensaje de bienvenida para el jugador
    def imprimeBienvenida(self):
        print("")
        print("Bienvenido al Mundo de Zuul")
        print("Zuul es un nuevo e increilemente aburrido juego de aventura")
        print("")
        print("Tu estas en "+ self.escenaActual.getDescripcion())
        print("Salidas: ")
        if self.escenaActual.salidaNorte != None:
            print("norte")
        if self.escenaActual.salidaEste != None:
            print("este")
        if self.escenaActual.salidaSur != None:
            print("sur")
        if self.escenaActual.salidaOeste != None:
            print("oeste")
        print("")
        
        # ...Codigo omitido...
        
    "--------------------- Clase Juego 3 ---------------------------------"
    
    # Intentar ir en una direccion.
    # Si hay una salida, entrar a la nueva escena; sino imprimir mensaje de error
    def irAEscena(self, comando):
        if not comando.tieneSegundoMundo():
            # Si no hay segundo mundo no sabemos donde ir
            print(" Ir a donde?")
            return
        direccion = comando.getSegundoMundo()
        # Intentar salir de la escena
        sgteEscena = None
        if direccion.equals("Norte"):
            sgteEscena = self.escenaActual.salidaNorte
        if direccion.equals("Este"):
            sgteEscena = self.escenaActual.salidaNorte
        if direccion.equals("Sur"):
            sgteEscena = self.escenaActual.salidaSur
        if direccion.equals("Oeste"):
            sgteEscena = self.escenaActual.salidaOeste
        if sgteEscena == None:
            print("No hay puerta")
        else:
             "------------------- Clase Juego 4 --------------------------------------"