list = [1,2,4,4,1,4,2,6,2,9]
# list = int(input("Ingrese varios numeros, y el programa se encaragara de eliminar los elementos que se repitan: "))
# list = []
new_list = []

for i in list:
    if i in list:
        del list[i]
        new_list.append(i)
        
    
print("La lista con elementos únicos:")
list.sort()
print(list)

# temps = [[0.0 for h in range(24)] for d in range(31)]


 
# total = 0.0
 
# for day in temps:
#     total += day[11]
 
# average = total / 31
 
# print("Temperatura promedio al mediodía:", average)
 
# table = [[":(", ":)", ":(", ":)"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]
 
# print(table)
# print(table[0][0])  # output: ':('
# print(table[0][3])  # output: ':)'
 