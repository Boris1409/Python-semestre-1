# capitalizaFrases: str -> str
# Recibe una cadena con varias oraciones separadas por “.”, donde todas sus letras están en
# mayúsculas y entrega la misma cadena pero con la primera letra de cada oración en mayúsculas
# y las demás en minúsculas.
#- Ej.: capitalizaFrases(“HOLA.QUE BIEN QUE HOY NO LLOVIO TANTO.CUIDATE.”),
# debe entregar: “Hola.Que bien que hoy no llovio tanto.Cuidate.”

def capitalizaFrases(textoMayusc):
    text_capitalized = ''
    texto_separado = textoMayusc.split('.')
    texto_limpio = [frase for frase in texto_separado if frase]

    for i in texto_limpio:
        text_capitalized += i.capitalize() + '.'

    if not textoMayusc.endswith('.'):
        final_text = text_capitalized.rstrip('.')
    else:
        final_text = text_capitalized
    return final_text

# Se muestra el uso del codigo 
ejemplo_de_frase = "HOLA.QUE BIEN QUE HOY NO LLOVIO TANTO.CUIDATE."
resultado = capitalizaFrases(ejemplo_de_frase)
print(resultado)

# SE CONFIRMA SI NO HAY ERROES CON UN ASSERT
assert resultado == 'Hola.Que bien que hoy no llovio tanto.Cuidate.'

