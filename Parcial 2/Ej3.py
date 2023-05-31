"""Se cuenta con dos sets: el primero contiene las temperaturas mínimas tomadas el mes de
Mayo en Osorno. El segundo set contiene las temperaturas máximas: (40 Puntos)
Temperaturas Mínimas = {9, 5, 2, 7, 6, 1}
Temperaturas Máximas = {12, 14, 11, 10, 15, 9}
A) Verificar si la temperatura 9°C está en ambos sets
B) Comprobar si al menos la temperatura 6°C y 17°C está en alguno de los sets
C) Elevar a 4 todas las temperaturas dentro de los sets
D) Unir ambos sets en uno solo"""

Temp_min = {9,5,2,7,6,1}
Temp_max = {12,14,11,10,15,9}
   
print("\n### - VERIFICAR SI LA TEMPERATURA 9° ESTA EN AMBOS SETS - ###")
if 9 in Temp_min and 9 in Temp_max:
    print("La temperatura 9°C está en los dos sets de temperaturas")
else:
    print("La temperatura 9°C está en un solo set de temperaturas")
    
print("\n### - COMPROBAR SI AL MENOS L TEMPERATURA 6°C Y 17°C ESTÁ EN ALGUNOS DE LOS SETS - ###")   
if 6 in Temp_min or 6 in Temp_max:
        print("La temperatura 6° se encuentra en un solo set de temperatura")
else:
    print("La temperatura 6° no se encuentra en ningun set de temperatura")
    
if 17 in Temp_min or 17 in Temp_max:
    print("La temperatura 17° esta en al menos un set de temperatura")
else:
    print("La temperatura 17° no esta en ningun set de temperatura")

print("\n### - ELEVAR A 4 TODAS LAS TEMPERATURAS DENTRO DE LOS SETS")
Temp_min_elevada = {temperatura_elevada **4 for temperatura_elevada in Temp_min}
Temp_max_elevada = {temperatura_elevada **4 for temperatura_elevada in Temp_max}
print(" sets con valores elevados",Temp_min_elevada)
print(" sets con valores elevados", Temp_max_elevada)

print("\n### - UNIR AMBOS SETS EN UNO SOLO - ###")
total = Temp_min_elevada.union(Temp_max_elevada)
print("La union de ambos sets queda así: ", total)

# for i in range(Temp_min):
#     i += 1
#     i == 9
#     print("La temperatura 9°C está en ambos sets")

# for i in range(1):
#     i == 17 in Temp_max.values()

# for i in range(1):
#     i == 17 in Temp_min.values()
#     print("La temperatura 17° no se encuentra en  ")
# else:
#     print("La temperatura 17° no se encuentra en ningun set")

    

