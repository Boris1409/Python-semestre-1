beatles = list()

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
beatles.append("Richard Starkey")

print("""\nTe presentamos a los integrantes que conforman
la banda de los BEATLES:\n""", 
      "\n1er Integrante:",beatles[0],
      "\n2do Integrante:",beatles[1],
      "\n3er Integrante:",beatles[2],
      "\n4er Integrante:",beatles[3],
      )

for i in range(1):
    print("""
          .__________________________________________________.
          |                                                  |
          | Porfavor, ingresa estos nombres ¡POR SEPARADO!:  |
          | 1.                                               |
          | 'Stu Sutcliffe'                                  |
          |                                                  |
          | 2.                                               |
          | 'Pete Best'                                      |
          |__________________________________________________|
          """)  
    
    nom_1 = input("\nIngrese el primer nombre: ")
    beatles.append(nom_1) 
    nom_2 = input("Ingrese el segundo nombre: ")
    beatles.append(nom_2)
    print("\nHasta el momento estos son los integrantes:",beatles)
    
print("Lo siento pero tendremos que eliminar a algunos integrantes de la banda")
del beatles[5]
del beatles[4]

print("\nQuieres agregar a un ultimo integrante a la banda?")
print(""" 
      SI
      NO
      """)

while True:
    opc = input()
    if opc == "SI":
        print("Gracias por tu respuesta")
        break
    elif opc == "Si":
        print("Entendido, gracias por tu respuesta")
        break
    elif opc == "si":
        print("Okey, gracias por tu respuesta")
        break
    elif opc == "NO":
        print("Vaya... aun así tenemos que agregarlo a la banda, pero gracias por tu respuesta")
        break
    elif opc == "No":
        print("Rayos... aun así, el se nos unirá, pero gracias.")
        break
    elif opc == "no":
        print("Bucha... igualmente el se integrará al grupo, adios.")
        break
    else:
        print("Responda como se indica porfavor")
        print("\n¿Cual es su respuesta?")
        continue
    
beatles.insert(0,"Ringo Starr")
          
print("\nDebido a su respuesta, el grupo quedo conformado por:",beatles)

