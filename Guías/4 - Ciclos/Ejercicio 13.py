'''
Escriba un programa que tome un número entero entre 0 y 100 provisto por el usuario e
imprima en la consola un mensaje indicando si el número es primo o no. Si el número no es un entero
entre 0 y 100, que imprima un mensaje indicando que el número ingresado no es entero entre 0 y
100.
'''
def number_de_0_a_100(n):
    if n >= 0 and n <= 100:
        test = False
        for i in range(2,n):
                if n % i == 0:
                     test = True
        if test:
            return False
        else:
            return True
    else:
        return False