"""
Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
imprima ¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
 """
 
var = input("Ingrese el nombre la planta: ")

if var == "ESPATIFILO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif var == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else: 
    print("¡Espatifilo!, ¡No", var, "!")