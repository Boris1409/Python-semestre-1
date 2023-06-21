Ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
ind_cal_aire = [134, 99, 245, 1]

min_ind_cal_aire = min(ind_cal_aire)
max_ind_cal_aire = max(ind_cal_aire)
ciudad_min = Ciudades[ind_cal_aire.index(min_ind_cal_aire)]
ciudad_max = Ciudades[ind_cal_aire.index(max_ind_cal_aire)]

print("Ciudad que posee el índice de calidad de aire más bajo es:", ciudad_min,"con un indice de:","-", min_ind_cal_aire, "-")
print("Ciudad que posee el índice de calidad de aire  más alto es:", ciudad_max, "con un indice de:","-", max_ind_cal_aire, "-")

if max_ind_cal_aire > 300:
    print("El índice de la calidad de aire está en la categoria |PELIGROSA|")
elif max_ind_cal_aire > 200:
    print("El índice de la calidad de aire está en la categoria |MUY DAÑINA PARA LA SALUD|")   
elif max_ind_cal_aire > 150:
    print("El índice de la calidad de aire está en la categoria |DAÑINA A ALA SALUD|")
elif max_ind_cal_aire > 100:
    print("El índice de la calidad de aire  está en la categoria |DAÑINA A LA SALUD PARA GRUPOS SENSIBLES|")
elif max_ind_cal_aire > 50:
    print("El índice de la calidad de aire  está en la categoria |MODERADA|")
else:
    print("El índice de la calidad de aire  está en la categoria |BUENA|")    
    
if min_ind_cal_aire > 300:
    print("El índice de la calidad de aire está en la categoria |PELIGROSA|")
elif min_ind_cal_aire > 200:
    print("El índice de la calidad de aire está en la categoria |MUY DAÑINA PARA LA SALUD|")   
elif min_ind_cal_aire > 150:
    print("El índice de la calidad de aire está en la categoria |DAÑINA A ALA SALUD|")
elif min_ind_cal_aire > 100:
    print("El índice de la calidad de aire está en la categoria |DAÑINA A LA SALUD PARA GRUPOS SENSIBLES|")
elif min_ind_cal_aire> 50:
    print("El índice de la calidad de aire está en la categoria |MODERADA|")
else:
    print("El índice de la calidad de aire está en la categoria |BUENA|")              