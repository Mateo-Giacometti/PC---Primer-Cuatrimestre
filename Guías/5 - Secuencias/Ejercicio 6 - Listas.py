'''
Hay un lenguaje de programación con sólo cuatro operaciones y una variable, x, definido por los
siguientes items:

Inicialmente, el valor de x siempre es 0.

++x y x++ incrementa el valor de la variable x en 1.

--x y x-- decrementa el valor de la variable x en 1.

Dada una lista de cadenas que contienen una lista de operaciones, devuelva el valor final de x después de
realizar todas las operaciones.
'''
def program(languaje: str, result = 0) -> int:
    for i in languaje:
        if i == '++x' or i == 'x++':
            result += 1
        elif  i == '--x' or i == 'x--':
            result -= 1
        elif i == '':
            result += 0
        else:
            return print('Error')
    return result
        
        