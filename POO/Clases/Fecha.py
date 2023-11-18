# ATRIBUTOS:
# dia: int
# mes: int
# año: int

class Fecha:
    def __init__(self, x):
        (dia, mes, año) = x.split("/")
        (self.dia, self.mes, self.año) = (int(dia), int(mes), int(año))
    
    # __Str__: -> str
    def __str__(self):
        # OPERADOR "+" COMCATENA strs
        return str(self.dia) + "/" + str(self.mes) + "/" + str(self.año)
    
    def siguiente(self):
        # INICIALIZADA d, m y a 
        d = self.dia; m = self.mes; a = self.año 
        
        # CASO 1: CAMBIO DE DIA DENTRO DE UN  MISMO MES 
        diaMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if d < diaMes[m-1]:
            d = d + 1
        
        # CASO 2: CAMBIO DE MES
        else:
            d = 1
            if m < 12:
                m = m + 1
                # CASO 3: CAMBIO DE AÑO 
            else:
                m = 1
                a = a + 1
            return Fecha(str(d)+"/"+(str(m)+"/")+(str(a)))
            

f = Fecha("01/5/2013")
print(f)    