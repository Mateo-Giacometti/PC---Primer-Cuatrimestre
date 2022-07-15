def cuartos():
    a = int(input('Ingrese mes: '))
    if 1 <= a <= 3:
        print('Usted esta en el Q1')
    elif 4 <= a <= 6:
        print('Usted este en el Q2')
    elif 7 <= a <= 9:
        print('Usted esta en el Q3')
    elif 10 <= a <= 12:
        print('Usted esta en el Q4')
    else:
        print('Error, cargue nuevamente le programa y ingrese un numero entre 1 y 12')
cuartos()