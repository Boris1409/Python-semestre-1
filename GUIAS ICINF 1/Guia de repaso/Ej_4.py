"""Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
en la letra inicial como en la final. Por ejemplo, si los nombres ingresados son
Belinda y Beatriz, se mostrara un mensaje que indique que ambos nombres comienzan con la misma letra. Si los nombres son Leonardo y Gonzalo, se mostrar´a
un mensaje que indique que ambos nombres terminan con la misma letra."""

nom1 = input("Ingrese su nombre: ")
nom2 = input("Ingrese el nombre de otra persona: ")

for letras in range(1):
    if nom1[0] != nom2[0]:
        print("Los nombres no comienzan cn la misma letra")
    else:
        print("Ambos nombres comienzan con la misma letra")
        break

for letras in [-1]:
    if nom1[-1] != nom2[-1]:
        print("Los nombres no terminan con la misma letra")
    else:
        print("Ambos nombres terminan con la misma letra")