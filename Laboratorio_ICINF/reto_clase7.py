def reto_clase7(enunciado):
    dic_de_palabras = {}
    conteo_palabras = enunciado.split()
    for palabra in conteo_palabras:
        dic_de_palabras[palabra] = len(palabra)
        return dic_de_palabras
    
while True:
    frase = input("Ingrese una frase, y y le diremos cuantas palabras contiene y su longitud: ")
    if frase.isdigit():
        print("No se aceptan numeros, ingrese de nuevo")
        continue
    else:
        break
    
resultado = reto_clase7(frase)
print(resultado)