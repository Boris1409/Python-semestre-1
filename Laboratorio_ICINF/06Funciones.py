print("\n################ 01- FUNCIONES - ##############")


#DECLARANDO LA PRIMERA FUNCION
def mi_primera_funcion():
    print("Esta es mi primera funcion")
    
mi_primera_funcion()
    
print("\n####### 02- DECLARANDO UNA FUNCION Y UTILIZARLA - ########")

def concatenar(lista1, lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

print(concatenar(lista1,lista2))

print("\n############## 03- DECLARANDO UNA FUNCION MULTIPLICABLE ##########")

1.
def multiplicacion(num1,num2):
    return num1*num2
print(multiplicacion(5,5))

2.
def division(x,y):
    return x//y
print(division(10,5))

print("\n###### 04- DECLARANDO SUMAS Y RESTAS POR FUNCIONES ############")

1.
def suma(a,b):
    return a+b
print(suma(3,2))

2.
def resta(c,d):
    return c-d
print(resta(4,2))