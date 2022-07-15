'''
scriba una función que diga si un número es par o impar.

def is_even(number: int) -> bool:
'''
def is_even(number):
    if number / 2 == int(number / 2):
        return print('El numero es par')
    else:
        return print('El numero es impar')