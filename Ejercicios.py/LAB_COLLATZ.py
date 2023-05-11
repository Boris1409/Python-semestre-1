c0 =  int(input("Ingrese un numero: "))

while c0 <= 0:
    c0  = int(input("El numero debe ser natural y distinto de cero"))
    
pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 =  3 * c0 + 1
        
pasos += 1

print(c0)