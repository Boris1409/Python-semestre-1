hat = [1, 2, 3, 4, 5]
print("""
      |  AQUI SE MUESTRA LOS ELEMENTOS DE  |
      |  LA LISTA: """,hat, "       |","\n"                 
      )

num = int(input("Ingrese un numero entero para reemplazar el numero de en medio que es: "))
hat[2] = num 

print("La lista actualizada es esta: ",hat)
del hat[4]
print("\nA continuación se borrará el ultimo elemento de la lista actual...")
print("\nLa longitud de esta lista nueva es: ",len(hat))
print("La nueva lista es esta: ",hat) 