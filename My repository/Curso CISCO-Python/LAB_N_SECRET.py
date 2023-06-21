n_secret = 14

print(
"""
°~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~°
| Bienvenido a este divertido juego,     |
| se trata de adivinar el número secreto,|
| Ingresa un número entero y adivina el  |
| numero que he escogido...              |
| ¿ Cuál es el número secreto?           |
°~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~°
""")

while True:
    num = int(input("Ingrese un número entero: "))
    if num != n_secret:
        print(" Ja JA JA JA, ¡Estás atrapado en mi bucle!")
        print("Vuelve a ingresar otro numero","\n")
    else:
        print("Muy bien, eres libre ahora")
        print("""
    
              
              
              
              
              
              Vuelve pronto...
              
              
              
            
              """)
        break