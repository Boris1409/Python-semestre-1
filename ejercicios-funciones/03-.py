# 3. Escriba un programa que pida la anchura y altura de un rectángulo 
# y lo dibuje con caracteres producto (*):

altura = int(input("Indique la altura de la figura: "))
anchura = int(input("Indique la anchura de la figura: "))

for i in range(1,altura + 1): #Indicamos el ciclo que recorrera 'i' con base 1, en la variable altura hasta que se cumpla el numero indicado por consola
    for j in range(1,anchura + 1): #Hacemos lo mismo pero con 'j' 
        print(' *', end = '') # La maquina imprimirá '*' con un fin de salto ed linea end ''
    print(' ')      