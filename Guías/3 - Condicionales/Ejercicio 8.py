'''
Escribir un programa que dado un día del año (1 a 366) ingresado por el usuario, imprima el día
de la semana que le corresponde. Debe asumir que el año comenzó, por ejemplo, un domingo. 
Por ejemplo: si se ingresa '5', imprime 'jueves', si se ingresa '10' imprime 'martes', si se ingresa '294'
imprime 'sabado'
'''
num = int(input('Ingrese un dia: '))
while True:
    num = num - 7
    if num == 1:
        print('Domingo')
        break
    elif num == 2:
        print('lunes')
        break
    elif num == 3:
        print('Martes')
        break
    elif num == 4:
        print('Miercoles')
        break
    elif num == 5:
        print('Jueves')
        break
    elif num == 6:
        print('Viernes')
        break
    elif num == 7:
        print('Sabado')
        break
        
