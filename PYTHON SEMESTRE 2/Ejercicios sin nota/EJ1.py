"""Escriba en Python una funcion que calcule el promedio de notas contenidas en un arreglo."""

"""
Consideraciones especiales:
• No se permite funciones predefinidas en Python (de ciclos solamente).
• Implemente una version con while y otra con for. Estas versiones de las funciones deben llamarse
promWhile(...) y promFor(...) y deben recibir las notas en un arreglo.

"""

# SE DEFINE UNA FUNCIÓN QUE LEERA LAS NOTAS CONTENIDAS EN UN ARREGLO Y LES DARA UN VALOR PARA OPERARLASMAS TARDE.
def promWhile(notas):
    if len(notas) == 0:
        return 0  
    
    #SE CREAN DOS VARABLES, UNA VARIABLE PARA HACER TODA LA SUMA DE LAS NOTAS, Y OTRA PARA HACER EL CONTROL DE NUESTRO CICLO WHILE.
    suma_notas = 0
    contador = 0
    
    # SE CREA UN CICLO WHILE QUE CON LA FUNCION LEN IRÁ LEYENDO LAS NOTAS DENTRO DEL ARREGLO, MIENTRAS QUE CON LA VARIABLE CONTADOR IR AVANZANDO DE 1 EN 1 HASTA LLEGAR AL TOTAL DE NOTAS CONTENIDAS EN EL ARREGLO
    while contador < len(notas):
        suma_notas += notas[contador]
        contador += 1
    
    # DENTRO DE LA VARIABLE PROMEDIO, SE DIVIDIRA LA SUMATORIA DE LAS NOTAS POR LA CANTIDAD DE NOTAS DENTRO DEL ARREGLO
    promedio = suma_notas / len(notas)
    return promedio

# FINALMENTE SE CREA UNA LISTA CON LAS NOTAS QUE UNO QUIERA CALCULAR Y SE EJECUTA LA FUNCION DE PROMWHILE LLAMANDO A ESTA MISA PARA ASI OBTENER UN RESULTADO
notas = [1,1,1,7,7,7]
promedio = promWhile(notas)
print("""\n         - FUNCIÓN WHILE - 
    El promedio de notas es:""", promedio)
