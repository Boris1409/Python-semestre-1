def es_el_año(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

def dia_del_mes(año, mes):
    if año < 1582 or mes < 1 or mes > 12:
        return None
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = dias[mes - 1]
    if mes == 2 and es_el_año(año):
        res = 29
        return res

def dia_de_año(año, mes, dia):
    dias = 0
    for m in range(1, mes):
        md = dia_del_mes(año, m)
        if md == None:
            return None
        dias += md
        md = dia_del_mes(año, mes)
        if dia >= 1 and dia <= md:
            return dias + dia
        else:
            return None
        
print(dia_de_año(2000, 12, 31))

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#         if md == None:
#             return None
#         days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None

# print(day_of_year(2000, 12, 31))
