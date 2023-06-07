def cantidad_de_numeros():
    while True:
        cantidad = input("Ingrese la cantidad de numeros que desea ingresar: ")
        if cantidad.isalpha():
            print("No se pueden imprimir numeros en cantidad negativo, ingrese denuevo")
            continue
        else:
            break
    return cantidad

cantidad_de_numeros()