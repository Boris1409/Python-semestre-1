año = int(input("Ingrese el año: "))
if año <= 1582:
    print("No esta dentro del periodo del calendario gregoriano")
else:
    if año % 4 != 0:
        print("Es un año común")
    elif año % 100 != 0:
        print("Es año bisiesto")
    elif año % 400 != 0:
        print("Es año comun")
    else:
        print("Es año bisiesto jsjsjs") 

