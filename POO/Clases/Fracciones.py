def dialogo():
    print("Suma y mayor de fracciones a/b y c/d")
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    d = int(input("d? "))
    print(f"suma = {suma_fracciones(a,b,c,d)}")
    print(f"mayor = {comparacion_fracciones(a,b,c,d)}")
    
def suma_fracciones(a,b,c,d):
    numerador = (a*d+c*b)
    denominador = b*d
    fraccion = (f"{numerador}/{denominador}")
    return fraccion

def comparacion_fracciones(a,b,c,d):
    if a*d > c*b:
        return f"{a}/{b}"
    else: 
        return f"{c}/{d}"
dialogo()
