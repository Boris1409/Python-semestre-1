#Este es un ejemplo de uso en método de lista
# Permiten manipular y acceder a elementos en una lista.

numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros) #  Resultado ->[1, 2, 3, 4, 5, 6]
print(numeros[2:4]) # Resultado -> [3, 4]

print(""" 
      METODO 2
      """)

1.
num = [111, 7, 2, 1]
print(len(num))
print(num)

2.
num.append(33) #CON .APPEND AGREGAMOS UNA VARIABLE, Y AUTOMATICAMENTE SE EXTIENDE LA LISTA COLOCANDOSE EN LA ULTIMA POSICION
print("\n",len(num))
print(num)

3.
num.insert(0, 11) #CON .INSERT INDICAMOS EN LA POSICION QUE QUEREMOS AGREGAR EL VALOR DESEADO, Y DESPUES LA VARIABLE QUE QUEREMOS INGRESAR
print("\n",len(num))
print(num)

4.
num.insert(1, 95)
print("\n",len(num))
print(num)

print("""
      CREANDO LISTA VACIA Y 
      AGREGAMDO ELEMENTOS A ELLA
      """)

new_list = []  # Creando una lista vacía.

for i in range(10):
    new_list.insert(0, i + 1)

print(new_list)

print(""" 
      HACIENDO USO DE LISTAS CON FOR
      """)

my_list = [10, 1, 8, 3, 5]
total = 0 
for i in range(len(my_list)):
    total += my_list[i]
    
    print(total) # TODO ESTE PROCESO MUESTRA PASO POR PASO LOS RESULTADOS

var1 = 1
var2 = 2

#########################

auxiliary = var1
var1 = var2 
var2 = auxiliary

########################

var_1 = 1
var_2 = 2

var_1, var_2 = var_2, var_1

print("""
      CREANDO UNA LISTA E INTERCAMBIAR
      EL ORDEN DE LOS ELEMENTOS
      """)

musica = ["PHONK", "ROCK", "80`s", "METAL"]
print("""
      ESTA ES LA LISTA DE MUSICA=  """ ,musica)

musica[0], musica[3] = musica[3], musica[0]
musica[1], musica[2] = musica[2], musica[1]

print("\nEl nuevo orden de la lista es: ", musica)

# for i in range(musica // 2):
#     musica[i], musica[musica - i - 1] = musica[musica - i - 1], musica[i]
 
# print(musica)
 