def es_año_bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True
        
test_data = [2004, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    año = test_data[i]
    print(año,"-> ",end="")
    result = es_año_bisiesto(año)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


