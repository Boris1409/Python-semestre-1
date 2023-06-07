def cantidad_de_numeros():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de números que desea ingresar: "))
            if cantidad <= 0:
                print("No se pueden ingresar una cantidad negativa de números. Ingrese nuevamente.")
                continue
            else:
                break
        except ValueError:
            print("ERROR, Ingrese nuevamente el número.")
    return cantidad

def escribir_cantidad_de_numeros(cantidad):
    list_num = []
    suma = 0
    for i in range(cantidad):
        while True:
            try:
                numero = int(input("Escriba el número: "))
                list_num.append(numero)
                suma += numero
                suma = sum(list_num)
                break
            except ValueError:
                print("ERROR, Ingrese nuevamente el número.")
    print("Esta es la lista que guarda todos los numeros ingesados",list_num)
    print("La suma total de los números ingresados es:", suma)
    return list_num

def suma_de_pares(list_num):
    suma = 0
    for numero in list_num:
        if numero % 2 == 0:
            suma += numero
    return suma

numeros_ingresados = escribir_cantidad_de_numeros(cantidad_de_numeros())
suma_pares = suma_de_pares(numeros_ingresados)
print("La suma de los números pares es:", suma_pares)
