#%%
'''
Escribir funciones que resuelvan los siguientes problemas
'''
#Dado un año indicar si es bisiesto.
def año_bisiesto(year: int) -> str:
    if ((year % 4) == 0) and ((year % 100) != 0) or (year == 400):
        return print('El año',year,'es bisiesto')
    else:
        return print('El año',year,'no es bisiesto')
#%%
#Dado un mes y un año, devolver la cantidad de días correspondientes. 
def month_days(year: int,month: int) -> int:
    if ((year % 4) == 0) and ((year % 100) != 0) or (year == 400):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        if month == 2:
            return 29
    elif ((year % 4) != 0):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        if month == 2:
            return 28
    if month > 12:
        return print('Error')
#%%
#Dada una fecha (día, mes, año), indicar si es válida o no.
def date(day: int,month: int,year: int) -> bool:
    if ((year % 4) == 0) and ((year % 100) != 0) or (year == 400):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day <= 31:
            return True
        if month == 4 or month == 6 or month == 9 or month == 11 and day <= 30:
            return True
        if month == 2 and day <= 29:
            return True
        else:
            return False
    elif ((year % 4) != 0):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day <= 31:
            return True
        if month == 4 or month == 6 or month == 9 or month == 11 and day <= 30:
            return True
        if month == 2 and day <= 28:
            return True
        else:
            return False
    if month > 12 or day > 31:
        return False
#%%
#Dada una fecha, indicar los días que faltan hasta fin de año.
def end_of_the_year(day: int,month: int,year: int) -> str:
    if month > 12 or day > 31:
        return False  
    elif ((year % 4) == 0) and ((year % 100) != 0) or (year == 400):
        long = 0
        if (((month == 2) and (day > 29)) or ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 
        or month == 10 or month == 12) or (day > 31)) and ((month == 4 or month == 6 or month == 9 or month == 11) 
        and (day > 30))):
            return False
        else:
            for i in range (1,month):
                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                    long += 31
                if i == 4 or i == 6 or i == 9 or i == 11:
                    long += 30
                if i == 2:
                    long += 29
            long = long + day
            return 366 - long
    elif ((year % 4) != 0):
        long = 0
        if (((month == 2) and (day > 28)) or ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 
        or month == 10 or month == 12) or (day > 31)) and ((month == 4 or month == 6 or month == 9 or month == 11) 
        and (day > 30))):
            return False
        else:
             for i in range (1,month):
                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                    long += 31
                if i == 4 or i == 6 or i == 9 or i == 11:
                    long += 30
                if i == 2:
                    long += 28
             long = long + day
             return 365 - long
#%%
#Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
def duration(day: int,month: int,year: int) -> str:
    if month > 12 or day > 31:
        return False  
    elif ((year % 4) == 0) and ((year % 100) != 0) or (year == 400):
        long = 0
        if (((month == 2) and (day > 29)) or ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 
        or month == 10 or month == 12) and (day > 31)) or ((month == 4 or month == 6 or month == 9 or month == 11) 
        and (day > 30))):
            return False
        else:
            for i in range (1,month):
                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                    long += 31
                if i == 4 or i == 6 or i == 9 or i == 11:
                    long += 30
                if i == 2:
                    long += 29
            long = long + day
            return long
    elif ((year % 4) != 0):
        long = 0
        if (((month == 2) and (day > 28)) or ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 
        or month == 10 or month == 12) and (day > 31)) or ((month == 4 or month == 6 or month == 9 or month == 11) 
        and (day > 30))):
            return False
        else:
             for i in range (1,month):
                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                    long += 31
                if i == 4 or i == 6 or i == 9 or i == 11:
                    long += 30
                if i == 2:
                    long += 28
             long = long + day
             return long 
#%%
#Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.      
def difference(day1, month1, year1, day2, month2, year2):
    if month1 > 12 or day1 > 31 or month2 > 12 or day2 > 31:
        return print('Una de las fechas no existe')  
    elif ((year1 % 4) == 0) and ((year1 % 100) != 0) or (year1 == 400):
        if (((month1 == 2) and (day1 > 29)) or ((month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 
        or month1 == 10 or month1 == 12) or (day1 > 31)) and ((month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11) 
        and (day1 > 30))):
            return print('Una de las fechas no existe') 
        
    elif ((year1 % 4) != 0):
        if (((month1 == 2) and (day1 > 28)) or ((month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 
        or month1 == 10 or month1 == 12) and (day1 > 31)) or ((month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11) 
        and (day1 > 30))):
            return print('Una de las fechas no existe')

    elif ((year2 % 4) == 0) and ((year2 % 100) != 0) or (year2 == 400):
        if (((month2 == 2) and (day2 > 29)) or ((month2 == 1 or month2 == 3 or month2 == 5 or month2 == 7 or month2 == 8 
        or month2 == 10 or month2 == 12) and (day2 > 31)) or ((month2 == 4 or month2 == 6 or month2 == 9 or month2 == 11) 
        and (day2 > 30))):
            return print('Una de las fechas no existe') 
        
    elif ((year2 % 4) != 0):
        if (((month2 == 2) and (day2 > 28)) or ((month2 == 1 or month2 == 3 or month2 == 5 or month2 == 7 or month2 == 8 
        or month2 == 10 or month2 == 12) and (day2 > 31)) or ((month2 == 4 or month2 == 6 or month2 == 9 or month2 == 11) 
        and (day2 > 30))):
            return print('Una de las fechas no existe')

    dif_year = abs(year1 - year2)
    dif_month = abs (month1 - month2)
    dif_day = abs(day1 - day2)
    return print('La diferencia entre cada fecha es de',dif_year,'años',dif_month,'meses y',dif_day,'dias')
#%%
       
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    