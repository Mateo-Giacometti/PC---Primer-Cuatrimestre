'''
Escriba una función que devuelva el producto entre dos números haciendo una suma repetida
(sin utilizar el operador de multiplicación * del lenguaje de programación).
'''
def producto(a,b):
    r = 0
    for i in range (0,b):
        r += a
    return r