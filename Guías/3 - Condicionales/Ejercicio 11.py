'''
Escribir un programa que inicie pidiendo al usuario que ingrese la fecha e imprima cuántos días
faltan para la primavera. Por ejemplo:
si el usuario ingresa el 2021-07-18 (18 de julio de 2021), faltan 65 días,
si ingresa el 2021-01-01 (1 de enero de 2021), faltan 263,
si ingresa el 2020-01-01 (1 de enero de 2020), faltan 264,
y si ingresa el 13 de noviembre de 2021, faltan 312 días.
'''
def sprint(day1, month1, year1):
    if month1 > 12 or day1 > 31:
        return print('La fecha no existe')  
    elif ((year1 % 4) == 0) and ((year1 % 100) != 0) or (year1 == 400):
        if (((month1 == 2) and (day1 > 29)) or ((month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 
        or month1 == 10 or month1 == 12) or (day1 > 31)) and ((month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11) 
        and (day1 > 30))):
            return print('La fecha no existe') 
        elif (day1 >= 21 and month1 == 9) or (day1 <= 21 and month1 == 12) or (month1 == 10) or (month1 == 11):
            return print('Estas en la primavera')
        else:
            if month1 <= 9 and day1 <= 21:
                new_month = abs(9 - month1)
                new_day = abs(21 - day1)
            elif (month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8) and day1 > 21:
                new_month = abs(8 - month1)
                new_day = abs(31 - day1 + 21)
            elif (month1 == 4 or month1 == 6) and day1 > 21:
                new_month = abs(8 - month1)
                new_day = abs(30 - day1 + 21)
            elif month1 == 2 and day1 > 21:
                new_month = abs(8 - month1)
                new_day = abs(29 - day1 + 21)
            if month1 == 12 and day1 > 21:
                new_month = 8
                new_day = abs(31 - day1 + 21)
     
    elif ((year1 % 4) != 0):
        if (((month1 == 2) and (day1 > 28)) or ((month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 
        or month1 == 10 or month1 == 12) and (day1 > 31)) or ((month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11) 
        and (day1 > 30))):
            return print('La fecha no existe')
        elif (day1 >= 21 and month1 == 9) or (day1 <= 21 and month1 == 12) or (month1 == 10) or (month1 == 11):
            return print('Estas en la primavera')
        else:
            if month1 <= 9 and day1 <= 21:
                new_month = abs(9 - month1)
                new_day = abs(21 - day1)
            elif (month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8) and day1 > 21:
                new_month = abs(8 - month1)
                new_day = abs(31 - day1 + 21)
            elif (month1 == 4 or month1 == 6) and day1 > 21:
                new_month = abs(8 - month1)
                new_day = abs(30 - day1 + 21)
            elif month1 == 2 and day1 > 21:
                new_month = abs(8 - month1)
                new_day = abs(28 - day1 + 21)
            if month1 == 12 and day1 > 21:
                new_month = 8
                new_day = abs(31 - day1 + 21)
    return print(f'Faltan {new_month} meses y {new_day} dias para la primavera')