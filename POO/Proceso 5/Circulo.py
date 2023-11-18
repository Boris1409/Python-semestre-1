pi = 3.14

# areaCirculo : num --> num
# Calcula el area del circulo usando la formula matematica ordinaria y solicitando el radio al usuario.
# ej: recibe 2 -> entrega 12.56

def areaCirculo(radio):
    area = pi*(radio**2)
    return area

# Test
assert areaCirculo(2) == 12.56


# pCirculo: num --> num
# Calcula el perimetro de un circulo usando la formula matematica ordinaria y solicitando el radio al usuario
# ej: recibe 3 -> entrega 18.84

def pCirculo(radio):
    perimetro = 2*pi*radio
    return perimetro

# Test
assert pCirculo(3) == 18.84
