resultado = ""
name = input("ingrese una palabra: ")
name = name.upper()

for letras in name:
    if name in "aeiou":
        continue
    resultado += name
    
print(resultado)