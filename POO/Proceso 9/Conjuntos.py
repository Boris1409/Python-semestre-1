# Clase Conjunto
# Atributos:
class Conjunto:
    def __init__(self,conjunto) -> None:
        assert type(conjunto) == list
        self.conjunto=conjunto
        
    def cardinal(self) -> int :
        return len(self.conjunto)
    
    def union(self,conjunto2):
        conjunto1=self.conjunto.copy()
        conjunto1.extend(conjunto2.conjunto)
        return Conjunto(list(set(conjunto1)))
    
    def interseccion(self,conjunto2) -> 'Conjunto':
        interseccionConjuntos=[]
        for i in self.conjunto:
            if i in conjunto2.conjunto:
                interseccionConjuntos.append(i)
        return Conjunto(interseccionConjuntos)
    
    def complemento(self) -> 'Conjunto':
        C=range(1,101)
        complementoConjunto=[]
        for i in C:
            if i not in self.conjunto:
                complementoConjunto.append(i)
        return Conjunto(complementoConjunto)
    
    def __str__(self) -> str:
        return f"Conjunto: {self.conjunto}"
    

X=Conjunto([1,3,5,6]) 
Y=Conjunto([1,2,4,5])
# cantidadReprobadosTareas: objecto,objeto -> int
# X,Y: objecto
# Se busca la cantidad de reprobados solo en tareas entre los
# aprobadosControles y aprobadosTareas.
# se obtiene que la interseccion de X e Y = N
# para luego obtener el complemento de N (los numeros del 1 al 100, 
# menos los de la interseccion de X e Y) = Ncom.
# Finalmente con la interseccion de Ncom se obtiene los reprobados
# solo por tareas y finalmente retorna la cantidad usando el metodo .cardinal()
# ej: X=[1,3,5,6] Y= [1,2,4,5]
# cantidadReprobadosTareas(X,Y) entrega 2
def cantidadReprobadosTareas(X,Y): # MI FORMA XD
    N=X.interseccion(Y)
    Ncom=N.complemento()
    reprobadosTareas=Ncom.interseccion(X)
    return reprobadosTareas.cardinal()


def cantidadReprobadosTareas2(X,Y): # MI FORMA 2.0
    return X.interseccion(Y).complemento().interseccion(X).cardinal()


def cantidadReprobadosTareas3(X,Y):
    return Y.complemento().interseccion(X) # FORMA DEL PROFE (ME DIJO UNION X PERO ERA INTERSECCION PROBABLEMENTE)