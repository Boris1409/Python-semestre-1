"""7. Determinar el factorial de un numero n, donde: 
n! = n · (n - 1) · (n - 2)..,3 · 2 · 1 (2.2)
factorial(x) = 
1 si x = 0
x · factorial(x - 1) si x ≥ 1
"""

print("BIENVENIDO AL PROGRAMA QUE CALCULA EL FACTORIAL DE UN NUMERO")
print("Ingrese el numero al que le desea calcular el factorial")
num = int(input())

base_factorial = 1
for numero_factorial in range(1, num+1):
    base_factorial*=numero_factorial 
print("El factorial de ",num, "es: ", base_factorial)