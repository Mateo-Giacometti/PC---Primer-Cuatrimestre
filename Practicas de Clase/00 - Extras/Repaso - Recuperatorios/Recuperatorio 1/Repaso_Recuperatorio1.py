# %%
#Guia de Funciones - Ejercicio 7
"""
Escriba una función que redondee un número de tipo flotante al entero más cercano y devuelva
este número entero.
"""
from hashlib import new
from tkinter.messagebox import RETRY
from typing import final

from pytest import console_main


def redondeo(n: float) -> int: 
    if n <= (int(n) + 0.5):
        return int(n)
    else:
        return int(n) + 1
# %%
#Guia de Funciones - Ejercicio 14
"""
Escriba una función que dado un tiempo en segundos, retorne el tiempo en horas, minutos y
segundos (similar al ejercicio 12). Por ejemplo, para 3745 debe devolver 1, 2, 25.
"""
def time(secs: int) -> tuple:
    hours, minutes, seconds = 0, 0, 0
    while secs >= 0:
        if secs >= 3600:
            hours += 1
            secs -= 3600
        elif secs >= 60: 
            minutes += 1
            secs -= 60
        else:
            seconds = secs
            break
    return hours, minutes, seconds
# %%
#Guia de Funciones - Ejercicio 13
"""
Escriba una función que dado un número devuelva el primer número múltiplo de 10 inferior o
igual a él. Por ejemplo, para 153 debe devolver 150.
"""
def muliplo(n: int) -> int:
    while n % 10 != 0:
        n -= 1
    return n 
# %%
#Guia de Condicionales - Ejercicio 10 
"""
Escribir funciones que resuelvan los siguientes problemas:
-Dado un año indicar si es bisiesto.
-Dado un mes y un año, devolver la cantidad de días correspondientes (por ejemplo: 2022 y 11
devuelve 30).
-Dada una fecha (día, mes, año), indicar si es válida o no.
-Dada una fecha, indicar los días que faltan hasta fin de mes.
-Dada una fecha, indicar los días que faltan hasta fin de año.
-Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
-Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre
ambas, en años, meses y días.
"""
def bisiesto(year: int) -> bool:
    if year % 4 == 0:
        return True 
    else:
        return False 

def days_in_months(year: int, month: int) -> int:
    if month in (4,6,9,11):
        return 30
    elif month in (1,3,5,7,8,10,12):
        return 31
    elif month == 2 and bisiesto(year) == True:
        return 29
    elif month == 2 and bisiesto(year) == False:
        return 28
    else:
        return False

def date_validation(year: int, month: int, day: int) -> bool:
    if days_in_months(year, month) >= day:
        return True
    else:
        return False

def end_of_the_month(year: int, month: int, day: int) -> int:
    if date_validation(year, month, day) == True:
        return (days_in_months(year, month) - day)
    else:
        return False

def end_of_the_year(year: int, month: int, day: int) -> int:
    if date_validation(year, month, day) == True:
        if bisiesto(year) == True:
            return 366 - course_of_the_year(year, month, day)
        else:
            return 365 - course_of_the_year(year, month, day)
    else:
        return False

def course_of_the_year(year: int, month: int, day: int) -> int:
    if date_validation(year, month, day) == True:
        course = day
        for i in range(1, (month)):
            course += days_in_months(year, i)
        return course
    else:
        return False

def difference_between_dates(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    if date_validation(year1, month1, day1) == date_validation(year2, month2, day2):
        if year1 > year2:
            diference = end_of_the_year(year2, month2, day2) + course_of_the_year(year1, month1, day1)
            if ((diference > 365 and bisiesto(year1) == False) or (diference > 366 and bisiesto(year1) == True)) and (year1 - year2) != 1:
                return diference
            else:
                year2 += 1
                while year1 != year2:
                    if bisiesto(year2) == True:
                        diference += 366
                        year2 += 1
                    else:
                        diference += 365
                        year2 += 1
                return diference
        elif year1 < year2:
            diference = end_of_the_year(year1, month1, day1) + course_of_the_year(year2, month2, day2)
            if ((diference > 365 and bisiesto(year2) == False) or (diference > 366 and bisiesto(year2) == True)) and (year2 - year1) != 1:
                return diference
            else:
                year1 += 1
                while year1 != year2:
                    if bisiesto(year1) == True:
                        diference += 366
                        year1 += 1
                    else:
                        diference += 365
                        year1 += 1
                return diference
        else:
            return abs(course_of_the_year(year1,month1, day1) - course_of_the_year(year2, month2, day2))
    else:
        return False

#Guia de Condicionales - Ejercicio 11
"""
Escribir un programa que inicie pidiendo al usuario que ingrese la fecha e imprima cuántos días
faltan para la primavera. Por ejemplo:
-Si el usuario ingresa el 2021-07-18 (18 de julio de 2021), faltan 65 días.
-Si ingresa el 2021-01-01 (1 de enero de 2021), faltan 263.
-Si ingresa el 2020-01-01 (1 de enero de 2020), faltan 264.
-Si ingresa el 13 de noviembre de 2021, faltan 312 días.
""" 
def spring(year: int, month: int, day: int) -> int:
    if date_validation(year, month, day) == True:
        if month <= 9:
            if day >= 21 and month == 9:
                return 0
            else:
                return ((course_of_the_year(year , 9, 21)) - course_of_the_year(year, month, day))
        elif month >= 12:
            if day <= 20 and month == 12:
                return 0 
            else:
                return ((course_of_the_year(year , 9, 21)) + end_of_the_year(year, month, day))
        else:
            return 0
    else:
        return False
# %%
#Guia de Secuencias - Tuplas - Ejercicio 2
"""
Escribir una función que reciba una fecha en formato AAAA-MM-DD y retorne un tupla de 3 enteros
con la fecha. En el formato AAAA-MM-DD, AAAA representa el año con 4 dígitos, MM el mes con 2 dígitos, y
DD el día con 2 dígitos.
"""
def date(fecha: str) -> tuple:
    fecha = fecha.replace('-','')
    if len(fecha) != 8:
        return print('Colocaste mal la fecha. Vuelve a intentarlo')
    year = int(fecha[0:4])
    month = int (fecha[4:6])
    day = int(fecha[6:])
    return (year, month, day)

# %%
#Guia de Secuencias - Tuplas - Ejercicio 3
"""
Escribir una función que reciba una lista de tuplas, donde cada tupla contiene un nombre y una fecha
(la fecha puede ser una tupla o una cadena en formato AAAA-MM-DD, a elección de quien programa la
función). La función debe retornar True si todas las personas son de sagitario. Considere el caso particular
en que la lista contenga 8 tuplas, los primeros 6 nombres sean "Gachi", "Pachi", "Lorena", "novio", "exnovio"
y "Andrea", y sean todos de sagitario, en cuyo caso debe imprimirse un mensaje acorde, además de retornar
el correspondiente True.
"""
#Formato AAAA-MM-DD"
def sagitario(lista: list) -> bool:
    for i in lista:
        if (int(i[1][5:7]) == 11 and (22 <= int(i[1][8:]) <= 30)) or (int(i[1][5:7]) == 12 and (1 <= int(i[1][8:]) <= 21)):
            continue
        else:
            return False
    return True
sagitario([("Gachi", "2004-11-29"),("pachi", "2004-08-12")])

#Formato con fecha en tuplas
def sagittarius(lista: list) -> bool:
    for i in lista:
        if ((i[1][1] == 11) and (22 <= i[1][2] <= 30)) or ((i[1][1] == 12) and (1 <= i[1][2] <= 21)):
            continue
        else:
            return False
    return True
sagittarius([("Gachi", (2004, 11, 29)),("pachi", (2004, 12, 12))])

# %%
#Primer Parcial - Ejercicio 6
def promedio(lista: list, n: int) -> list:
    new_list = []
    sum = 0
    while len(lista) >= n:
        for i in range(0,n):
            sum += lista[i]
        new_list.append((sum/n))
        lista.remove(lista[0])
        sum = 0
    return new_list
promedio([7,9,3,6,6,2], 4)

# %%
#Primer Parcial - Ejercicio 8
def books(book_list: list, ISBN: str) -> list:
    autor = ''
    autor_list = []
    for i in book_list:
        if (i[0].replace('-','')) == (ISBN.replace('-','')):
            autor += i[2]
            break
    for v in book_list:
        if v[2] == autor:
            autor_list.append(v)
    return autor_list

books([('978-0137081073', 'The Clean Coder', 'Robert Martin', 40, 'Software desing'), ('978-0-13-235088-4', 'Clean Code', 'Robert Martin', 45, 'Software test'), ('9780135957059', 'The Pragmatica Programmer', 'Andrew Hunt', 30, 'Software test')], '978-013708-1073')
# %%
#Guia de de Secuencias - Cadenas - Ejercicio 7
"""
Queremos acortar el largo de un mensaje para que entre en una cantidad fija de caracteres, n. Si el
mensaje tiene más de n caracteres, es decir, no entra en n caracteres, entonces eliminaremos el excedente
y lo completaremos con "." hasta completar los n caracteres, y a lo sumo 3 puntos.
"""
def cifrado(m: str, n: int) -> str:
    cif = ''
    final_cif = ''
    if len(m) >= 1 and n >= 1:
        for i in range(0,n):
            if i <= 2:
                cif += '.'
            else:
                final_cif += m[(i-3)]
        return final_cif + cif
    else:
        return ""
mensaje = str(input('Escriba un mensaje: '))
cifras = int(input('Escriba los caracteres permitidos: '))
cifrado(mensaje, cifras)
# %%
#Guia de de Secuencias - Cadenas - Ejercicio 8
"""
Programar una función que retorne True si un password (string) cumple con los siguientes
requisitos:
Tiene que tener por lo menos una letra minúscula.
Tiene que tener por lo menos una letra mayúscula.
Tiene que tener por lo menos un número.
Tiene que tener por lo menos un signo no alfanumérico (p.ej. ! ó $).
Tiene que tener entre 8 y 31 caracteres.
"""
def password(word: str) -> bool:
    m, M, num, noalf = 0, 0, 0, 0
    if len(word) >= 8 and len(word) <= 31:
        for i in word:
            if i.isupper() == True:
                M += 1
            elif i.islower() == True:
                m += 1
            elif i.isnumeric() == True:
                num += 1
            elif i.isalnum() == False:
                noalf += 1
        if m > 0 and M > 0 and num > 0 and noalf > 0:
            return True
        else:
            return False 
    else:
        return False 
call_password = str(input('Verifique si su contrase es segura: '))
password(call_password)
# %%
#Guia de de Secuencias - Listas - Ejercicio 8
"""
Programar una función que tome como argumento un párrafo (un string con muchas palabras), y
retorne una lista indicando la frecuencia con la que ocurren palabras de distinta longitud (la estructura de
la lista a retornar queda a criterio del diseñador, pero debe ser explicada claramente en el docstring). Es
decir, la función debe computar cuantas palabras de largo 1 hay en el párrafo, cuantas de largo 2, y así
sucesivamente hasta la longitud más larga que tenga el párrafo.

Nota: los signos de puntuación no son considerados parte de la palabra, así como cualquier otro
carácter que no sea una letra del abecedario.
"""
import operator
def parrafo(text: str) -> list:
    lista1 = text.split(' ')
    lista2 = []
    dic = {}
    final_dic = {}
    for i in lista1:
        if i.isalnum() == False or i.isnumeric() == True:
            for v in i:
                correction = ''
                if v.isalnum() == True and v.isnumeric() == False:
                    correction += v
            lista2.append(correction)
        else:
            lista2.append(i)
   
    for c in lista2:
        if len(c) >= 1:
            if len(c) in dic:
                dic[len(c)] = dic[len(c)] + 1
            else:
                dic[len(c)] = 1
    
    sortedDict = sorted(dic.items(), key=operator.itemgetter(0))

    for b in sortedDict:
        final_dic[b[0]] = b[1]
    
    return final_dic
# %%
#Guia de de Secuencias - Listas - Ejercicio 7
"""
Programar una función llamada terminan_en_vocal que tome por argumento una lista de strings,
y devuelva otra lista con los strings que terminan en vocal.
Pueden probar la función con las palabras que surgen de aplicar la función split al preámbulo de la
Constitución Nacional.
"""
def termina_en_vocal(lista: list) -> list:
    return_list = []
    for i in lista:
        if i[(len(i) - 1)].lower() in ('a','e','i','o','u'):
            return_list.append(i)
    return lista

coso = "Nos, los representantes del pueblo de la Nación Argentina, reunidos en Congreso General  Constituyente por voluntad y elección de las provincias que la componen, en cumplimiento de pactos preexistentes, con el objeto de constituir la unión nacional, afianzar la justicia, consolidar la paz interior, proveer a la defensa común, promover el bienestar general, y asegurar los beneficios de la libertad, para nosotros, para nuestra posteridad, y para todos los hombres del mundo que quieran habitar en el suelo argentino: invocando la protección de Dios, fuente de toda razón y justicia: ordenamos, decretamos y establecemos esta Constitución, para la Nación Argentina"
termina_en_vocal(coso.split(' '))
# %%
#Guia de de Secuencias - Cadenas - Ejercicio 12
"""
-Escribir una función que permita determinar si una cadena podría formar una palabra, del siguiente
modo: el carácter "?" sirve de comodín para cualquier letra, mientras que sea 1 (una) letra, por lo que "?oca"
puede formar la palabra "poca", también la palabra "boca", o "roca". La palabra "?" puede formar cualquier
cadena de largo 1, mientras que "?o?a" puede formar "poca", "bota", "rosa", etc.

-Siguiendo la misma idea, implemente una función que, además, considere al "*" como un
comodín para múltiples letras, de forma tal que "*ta" coincide contra cualquiera palabra que termina
en "ta", "r*ta" con cualquier palabra que comienza con "r" y termina con "ta", como "respuesta".
Considere el caso en que haya más de un comodín, por ejemplo, "est?rno*le*domas*d?o" que da True
para "esternocleidomastoideo".
"""
def matches(base: str, word: str) -> bool:
    if len(base) == len(word):
        for i in range(len(base)):
            if base[i] == word[i] or base[i] == '?':
                continue
            else:
                return False
        return True
    else:
        return False
# %%
#Guia de diccionarios - Ejercicio 8
"""
Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las
claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
"""
def orden(lista: list) -> dict:
    dic = {}
    for i in lista:
        if i[0] in dic:
            dic[i[0]] += [i[1]]
        else:
            dic[i[0]] = [i[1]] 
    return dic

l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días') ]
orden(l)
# %%
#Guia de diccionarios - Ejercicio 9
"""
Escribir una función que reciba la cantidad de iteraciones a realizar de una tirada de 2 dados y
devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.

Nota: utilizar el módulo random para obtener tiradas aleatorias.
"""
import random
def tirada_de_dados(tiros: int) -> dict:
    dic = {}
    for i in range(tiros):
        a = random.randint(1,6)
        b = random.randint(1,6)
        sum = a + b
        if sum in dic:
            dic[sum] += 1
        else:
            dic[sum] = 1
    return dic
# %%
#Guia de diccionarios - Ejercicio 10
"""
Implementamos una agenda con un diccionario, donde almacenamos nombres y números
telefónicos. Escribir un programa que vaya solicitando al usuario que ingrese nombres, luego:

1. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir
modificarlo si no es correcto.

2. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”*”, para salir del programa.
"""
def main():
    status = True
    dic = {'Mateo Giacometti': 3364180261,'Fausto Pettinari':3364230854,'Colo Schuemer':3364357698}
    while status:
        name = input('Ingrese un nombre: ')
        if name in dic:
            print('El contacto esta en tu agenda. Su numero de telefino es ',dic[name])
            while True:
                try:
                    y_o_n = input('Es correcto el numero ? (y or n): ')
                    if y_o_n !='y' and y_o_n !='n':
                        raise ValueError
                    break
                except ValueError:
                    print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
            if y_o_n == 'n':
                while True:
                    try:
                        y_o_n_2 = input('Desea cambiarlo ? (y or n): ')
                        if y_o_n_2 !='y' and y_o_n_2 !='n':
                            raise ValueError
                        break
                    except ValueError:
                        print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                if y_o_n_2 == 'y':
                    number = int(input('Ingrese el numero de telefono correcto: '))
                    dic[name] = number
                    while True:
                        try:
                            y_o_n_9 = input('Desea continuar ? (y or n): ')
                            if y_o_n_9 !='y' and y_o_n_9 !='n':
                                raise ValueError
                            break
                        except ValueError:
                            print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                    if y_o_n_9 == 'n':
                        status = False
                    else:
                        continue
                else:
                    while True:
                        try:
                            y_o_n_6 = input('Desea continuar ? (y or n): ')
                            if y_o_n_6 !='y' and y_o_n_6 !='n':
                                raise ValueError
                            break
                        except ValueError:
                            print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                    if y_o_n_6 == 'n':
                        status = False
                    else:
                        continue
            else:
                while True:
                    try:
                        y_o_n_3 = input('Desea continuar ? (y or n): ')
                        if y_o_n_3 !='y' and y_o_n_3 !='n':
                            raise ValueError
                        break
                    except ValueError:
                        print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                if y_o_n_3 == 'n':
                    status = False
                else:
                    while True:
                        try:
                            y_o_n_7 = input('Desea continuar ? (y or n): ')
                            if y_o_n_7 !='y' and y_o_n_7 !='n':
                                raise ValueError
                            break
                        except ValueError:
                            print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                    if y_o_n_7 == 'n':
                        status = False
                    else:
                        continue
        else:
            while True:
                    try:
                        y_o_n_4 = input('Este contacto no se encuentra en su agenda. Desea agregarlo ? (y or n): ')
                        if y_o_n_4 !='y' and y_o_n_4 !='n':
                            raise ValueError
                        break
                    except ValueError:
                        print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
            if y_o_n_4 == 'y':
                new_number = int(input('Ingrese el numero de telefono del contacto: '))
                dic[name] = new_number
                while True:
                    try:
                        y_o_n_8 = input('Desea continuar ? (y or n): ')
                        if y_o_n_8 !='y' and y_o_n_8 !='n':
                            raise ValueError
                        break
                    except ValueError:
                        print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                if y_o_n_8 == 'n':
                    status = False
                else:
                    continue
            else:
                while True:
                    try:
                        y_o_n_5 = input('Desea continuar ? (y or n): ')
                        if y_o_n_5 !='y' and y_o_n_5 !='n':
                            raise ValueError
                        break
                    except ValueError:
                        print("\nOops!  This instance doesn´t take letters or numbers outside y or n.  Try again...")
                if y_o_n_5 == 'n':
                    status = False
                else:
                    continue
    print('La agenda finaliza con este contenido:',dic)

if __name__=='__main__':
    main()
# %%
#Ejercicio de otro parcial
"""
Escribir una función que dado un dia del año (un número del 1 a 366) retorne el dia de la semana que le corres ponde. 
Debe asumir que el año comenzo, por ejemplo, un domingo Por ejemplo: si se ingresa 5, retorna jueves, si se ingresa 10 retorna 
martes, si se ingresa 294 retorna sabado
"""
def week_day(day: int) -> str:
    while day > 7:
        day -= 7
    if day == 1:
        return print('Domingo')
    elif day == 2:
        return print('Lunes')
    elif day == 3:
        return print('Martes')
    elif day == 4:
        return print('Miercoles')
    elif day == 5:
        return print('Jueves')
    elif day == 6:
        return print('Viernes')
    else:
        return print('Sabado')
# %%
#Ejercicio de otro parcial
"""
Un código secreto para cifrar textos consiste en tomar cada palabra y:

-Si comienza con una vocal, se agrega al final de la palabra pa, po, pi, po o pu en función vocal al inicio de la palabra
a con pa, e con pe, etc. Por ejemplo, acato se vuelve acatopa. 

-Si comienza con otra letra, y la palabra tiene menos de o exactamente 5 letras, se toma esa letra se agrega
al final, y se completa con ro Por ejemplo, 'de' se convierte en edro.

-Si la palabra no comienza con vocal pero tiene más de 5 letras, se toman las primeras tres letras, se pasan al final 
y se completa con re. Por ejemplo, 'función' se convierte en cionfunre.
"""
def patron(phrese: str) -> str:
    final_word = ''
    lista = phrese.split(' ')
    for i in lista:
        if i[0].lower() in ('a','e','i','o','u'):
            if i[0].lower() == 'a':
                new_word = i + 'pa' + ' '
                final_word += new_word 
            elif i[0].lower() == 'e':
                new_word = i + 'pe' + ' '
                final_word += new_word 
            elif i[0].lower() == 'i':
                new_word = i + 'pi' + ' '
                final_word += new_word 
            elif i[0].lower() == 'o':
                new_word = i + 'po' + ' '
                final_word += new_word 
            else:
                new_word = i + 'pu' + ' '
                final_word += new_word 
        elif len(i) <= 5:
            new_word = i[1:] + i[0] + 'ro' + ' '
            final_word += new_word 
        else:
            new_word = i[3:] + i[0:3] + 're' + ' '
            final_word += new_word 
    return print(final_word.strip())
# %%
#Ejercicio de otro parcial (Colo)
def aprobados(tps: list, parcial: list, nombres: list) -> list:
    return_list = []
    for i in range(len(nombres)):
        sum = 0
        for v in tps[i]:
            sum += v
        sum += parcial[i]
        final_sum = sum / 4
        if final_sum >= 4:
            return_list.append((nombres[i], final_sum))
    return return_list

aprobados([(1.2,2.5,3),(4, 5.7, 6),(5,4.1,6)], [9,5.2,1],['Ariel', 'Dani', 'Cami'])
# %%
#Ejercicio de otro parcial (Colo)
def ADN(nitro: str, base: str) -> str:
    for i in range(len(nitro)):
        if nitro[i:(i + len(base))] == base:
            adn = nitro[(i-3):i] + base + nitro[(i + len(base)):(i + len(base) + 10)]
            return print(adn)
        else:
            continue
    return print('')

ADN('tggaagctcagttggttccattacagagtgagactcgccg', 'catta')
