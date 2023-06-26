trabajadores = [
    ['Juan',[700000,650000,690000]], 
    ['María',[681000,710000,590000]], 
    ['Pedro',[590000,635000,705000]]
    ]

def promedio(trabajadores):
    promedio_juan  = sum(trabajadores[0][1]) / len(trabajadores[0][1])
    promedio_maria = sum(trabajadores[1][1]) /len(trabajadores[1][1])
    promedio_pedro = sum(trabajadores[2][1]) / len(trabajadores[2][1])
    
    print('Promedio de Juan es: ', round(promedio_juan,2))
    print('Promedio de Maria es: ', round(promedio_maria,2))
    print('Promedio de Pedro es: ', round(promedio_pedro,2))

def sueldo(trabajadores):
    sueldo_juan  = max(trabajadores[0][1])
    sueldo_maria = max(trabajadores[1][1])
    sueldo_pedro = max(trabajadores[2][1])
    
    print('El sueldo mas alto de Juan es: ', sueldo_juan)
    print('El sueldo mas alto de Maria es: ', sueldo_maria)
    print('El sueldo mas alto de Pedro es: ', sueldo_pedro)

totales_impuestos = ()

def retencion_impuestos(trabajadores):
    total_juan  = sum(trabajadores[0][1])
    total_maria = sum(trabajadores[1][1])
    total_pedro = sum(trabajadores[2][1])
    
    impuesto_juan  = total_juan * 0.1225
    impuesto_maria = total_maria * 0.1225
    impuesto_pedro = total_pedro * 0.1225
    
    retencion_impuestos = (impuesto_juan, impuesto_maria, impuesto_pedro)
    mayor_impuesto      = max(retencion_impuestos)
    
    print('La retencion de impuestos de Juan es ', impuesto_juan)
    print('La retencion de impuestos de Maria es ', impuesto_maria)   
    print('La retencion de impuestos de Pedro es ', impuesto_pedro) 
    print('\nEl mayor impuesto impuesto retenido es ', mayor_impuesto) 

print(' ')
promedio(trabajadores)
print(' ')
sueldo(trabajadores)
print(' ')
retencion_impuestos(trabajadores)