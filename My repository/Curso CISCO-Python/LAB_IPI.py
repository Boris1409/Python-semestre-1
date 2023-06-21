ipi = float(input("Ingrese su ingreso anual: "))

if ipi < 85528:
    imp = ipi * 0.18 - 556.02
else:
    imp = (ipi - 85528) * 0.32 + 14839.02
    
if imp < 0.0: 
    imp = 0.0
    
imp = round(imp,0) 
print("El impuesto total es de:", imp, "pesos")