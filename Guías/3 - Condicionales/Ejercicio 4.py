'''
Escriba una función que dados dos números a y b compare estos números y retorne otro
número indicando el resultado de la comparación del siguiente modo:

0, si a y b son iguales,

negativo, si a es menor que b,

positivo, si a es mayor que b.

def cmp_number(a: float, b: float) -> float:
 # complete m
'''
def cmp_number(a: float, b: float) -> str:
    if a > b:
        return print('positivo')
    elif a < b:
        return print('negativo')
    else:
        return 0
    
        