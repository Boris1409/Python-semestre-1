""" En las olimpiadas de invierno el tiempo que realizan los participantes en la competencia de velocidad en pista se mide en minutos , segundos y centesimas.
Construye un programa que calcule la velocidad de los participantes en kilometros por hora de las diferentes competencias.

Datos: DIS, MIN, SEG, CEN.
Donde: DIS es una variable de tipo entero que indica la distancia del recorrido. MIN es una variable de tipo entero que representa el numero de minutos. 

Considereaciones:
El tiempo debemos expresarlo en segundos, y para hacerlo aplicamos la siguiente formula:
TSE = MIN * 60 + SEG + CEN / 100 

Luego podemos calcular la velocidad expresada en metros sobre segundos (m/s): 
VMS = DIS(Metros) / TSE(Segundos) 

Para obtener la velocidad en kilometros por hora (k/h), aplicamos la siguiente formula: 
VKH = VMS * 3600(Kilometros) / 1000(Hora))"""

def datos():
    distancia  = int(input('Ingrese la distancia recorrida en metros '))
    minutos    = int(input('Ingrese la cantidad de minutos '))
    segundos   = int(input('Ingrese la cantidad de segundos '))
    centesimas = int(input('Ingrese la cantidad de centesimas '))
    return distancia, minutos, segundos, centesimas

def convertir_tiempo_segundos(minutos, segundos, centesimas):
    tse = (minutos * 60) + segundos + (centesimas / 100)
    return tse

def calcular_velocidad(distancia, tse):
    vms = distancia / tse
    return vms

def convertir_velocidad_kilo_hora(vms):
    vkh = (vms * 3600) / 1000
    print('\nLa velocidad en kilometos por hora es ',vkh,'km/h')
    


distancia, minutos, segundos, centesimas = datos()
tse = convertir_tiempo_segundos(minutos, segundos, centesimas)
vms = calcular_velocidad(distancia, tse)
vkh = convertir_velocidad_kilo_hora(vms)
