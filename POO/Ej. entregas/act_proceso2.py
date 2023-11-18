
#Area formula Heron: num -> float
#Ingresar(lado1,lado2,lado3), calcular y entregar valor del area de un triangulo
#ej: area_triangulo --> entrega: 59.00 (salida entrega 2 decimales)



lado1 = float(input("ingrse el primer lado: "))
lado2 = float(input("ingrse el segundo lado: "))
lado3 = float(input("ingrese el tercer lado: "))


def area_heron(lado1,lado2,lado3):
    p=(lado1+lado2+lado3)/2 
    A=(p*(p-lado1)*(p-lado2)*(p-lado3))**(1/2)

    return f"{A:.2f}"
        
print("el area del triangulo es",(area_heron(lado1,lado2,lado3)))
