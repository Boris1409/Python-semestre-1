import random 

numero_secreto = random.randint(0, 100)
intentos = 0
Adivinado = False

while intentos < 10 and not adivinado:
    intentos += 1
    respuesta = int(input("Intento #" + str(intentos) + ": Adivina el número (entre 1 y 100):"))
    if respuesta == numero_secreto:
        print("¡Has adivinado el numero en",intentos, "intentos!")
        adivinado = True
    elif respuesta < numero_secreto:
        print("El número es mayor.")
    else:
        print("EL número es menor.")
        if not adivinado:
            print("Lo siento, has agotado tus 10 intentos. El número era", numero_secreto)
            