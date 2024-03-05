class Guitarra:
    def __init__(self):
        self.iCuerda = 1
        self.iEspacio = 0
        self.cuerdas = {
            1: "Mi",
            2: "Si",
            3: "Sol",
            4: "Re", 
            5: "La",
            6: "Mi"
        }
        self.nota = "No hay nota definida"  
    def setDedo(self, posCuerda, posEspacio):
        if posCuerda not in self.cuerdas or posEspacio < 0:
            return False
        self.iCuerda = posCuerda
        self.iEspacio = posEspacio
        self.nota = self.cuerdas[posCuerda]  
        return True
    
    def getNota(self):
        return self.nota