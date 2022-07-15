'''
Escriba una función que pida un número x, luego pida otro y, y devuelva los dos números
multiplicados y divididos. En la consola debe imprimirse lo siguiente:

Ingrese el primer número: x

Ingrese el segundo número: y

El resultado de la multiplicación es x * y = z

El resultado de la división es x / y = w

Note que x e y están alineados a la misma distancia, es decir que están separados por un tab y no por
espacios.

¿Si x=1 e y=10, la división devuelve 0.1? (vea la diferencia entre int y float)

¿Qué pasa con la división si y=0? Agregue una verificación que se fije que y no sea 0. En caso de
que sea 0, que no haga ningún cálculo e imprima:

No se puede dividir por 0
'''
def calculos():
    x = float(input('Ingrese el primer número:   '))
    y = float(input('Ingrese el segundo número:  '))
    multiplicación = x * y
    if y != 0:
        division = x / y
    else:
        return print('\nNo se puede dividir por 0')
    return print('El resultado de la multiplicación es x * y =',multiplicación,
                 '\nEl resultado de la división es x / y =',division)
calculos()