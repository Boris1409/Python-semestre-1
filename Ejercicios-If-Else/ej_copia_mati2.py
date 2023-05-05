"""RETO PYTHON"""

# 3. Definir una función que reciba tres números enteros y devuelva el valor del mayor de ellos. Por ejemplo, para los números 5, 7 y 5, devolvería el
# valor 7.


def numero_mayor(num1, num2, num3):
    if num1 >= num2 and num3:
        return numero_mayor
    elif num2 >= num1 and num3:
        return numero_mayor
    elif num3 >= num2 and num1:
        return numero_mayor
    else:
        return numero_mayor
    
num_1 = int(input("Escriba el primer numero: "))
num_2 = int(input("Escriba el segundo numero: "))
num_3 = int(input("Escriba el tercer numero: "))
numero_mayor(num_1, num_2, num_3)