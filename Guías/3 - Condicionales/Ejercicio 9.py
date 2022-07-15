'''
Escribir una función que dadas dos rectas definidas por su pendiente y su ordenada al origen
devuelva la abcisa en la que se intersectan. Validar lo que considere necesario.
'''
def absisa():
    p_1 = float(input('Ingrese el valor de la pendiente de la primer recta:'))
    o_1 = float(input('Ingrese el valor de la ordenada al origen de la primer recta:'))
    p_2 = float(input('Ingrese el valor de la pendiente de la segunda recta:'))
    o_2 = float(input('Ingrese el valor de la ordenada al origen de la segunda recta:'))
    num = ((o_2 - o_1) / (p_1 - p_2))
    print('La absisa que las intersecta es:',num)
absisa()



