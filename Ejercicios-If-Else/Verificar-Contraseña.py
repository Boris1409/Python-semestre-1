"""Verificar si la contraseña es valida"""

def validar_contraseña(contra1):
    if len(contra1) < 4:
        return 
    
contra1 = input("Escriba su contraseña de 4 caracteres minimo: ")

if len(contra1) >= 4:
    print("La contraseña fue admitida")
else:
    print("La contraseña no es valida")
    



