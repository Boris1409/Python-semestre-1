print("---Paciente 1---")

while True:
    nombre1 = input("Ingrese el nombre del paciente: ")
    if nombre1.isnumeric() == True:
        print("Se requiere que tenga al menos 1 caracter")
    else:
        break
    
while True:
    peso1 = float(input("Ingrese el peso del paciente: "))
    if peso1 <= 0 or peso1 >= 400:
        print("La cantidad ingresada no puede ser aceptada, porfavor reingrese el peso del paciente")
    else:
        break  
    
while True:
    estatura1 = float(input("Ingrese la estatura del paciente: "))
    if estatura1 <= 0 or estatura1 > 210:
        print("La estatura es invalida, reingrese la estatura porfavor")
    else:
        break    
    
while True:
    edad1 = int(input("Ingrese la edad del paciente: "))
    if edad1 <= 0 or edad1 > 110:
        print("Edad invalida, porfavor reingrese la edad del paciente")
    else:
        break
    
tupla_1 = (nombre1,peso1, estatura1, edad1)
print(tupla_1)
print("\n")

print("---Paciente 2---")

while True:
    nombre2 = input("Ingrese el nombre del paciente 2: ")
    if nombre2.isnumeric() == True:
        print("Se requiere que tenga al menos 1 caracter")
    else:
        break
    
while True:
    peso2 = float(input("Ingrese el peso del paciente 2: "))
    if peso2 <= 0 or peso2 >= 400:
        print("La cantidad ingresada no puede ser aceptada, porfavor reingrese el peso del paciente 2")
    else:
        break  
    
while True:
    estatura2 = float(input("Ingrese la estatura del paciente 2: "))
    if estatura2 <= 0 or estatura2 > 210:
        print("La estatura es invalida, reingrese la estatura porfavor")
    else:
        break    
    
while True:
    edad2 = int(input("Ingrese la edad del paciente 2: "))
    if edad2 <= 0 or edad2 > 110:
        print("Edad invalida, porfavor reingrese la edad del paciente 2")
    else:
        break
    
tupla_2 = (nombre2,peso2, estatura2, edad2)
print(tupla_2)
print("\n")

print("---Paciente 3---")

while True:
    nombre3 = input("Ingrese el nombre del paciente 3: ")
    if nombre3.isnumeric() == True:
        print("Se requiere que tenga al menos 3 caracter")
    else:
        break
    
while True:
    peso3 = float(input("Ingrese el peso del paciente 3: "))
    if peso3 <= 0 or peso3 >= 400:
        print("La cantidad ingresada no puede ser aceptada, porfavor reingrese el peso del paciente 3")
    else:
        break  
    
while True:
    estatura3 = float(input("Ingrese la estatura del paciente 3: "))
    if estatura3 <= 0 or estatura3 > 210:
        print("La estatura es invalida, reingrese la estatura porfavor")
    else:
        break    
    
while True:
    edad3 = int(input("Ingrese la edad del Tercer paciente"))
    if edad3 <= 0 or edad3 >= 111:
        print("La edad es invalida, reingrese la edad")
    else:
        break
    
tupla_3 = (nombre3, peso3, estatura3, edad3)
print(tupla_3)