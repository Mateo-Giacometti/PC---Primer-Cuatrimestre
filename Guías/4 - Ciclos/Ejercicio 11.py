'''
Escriba una función que le pida al usuario ingresar 10 números enteros y que imprima el mayor
número impar de los ingresados. De no haber ingresado ningún número impar, que imprima un
mensaje para dar aviso.
'''
def numeros_impares(a):
    numeros_impares = []
    if len(a) > 10:
        return 'Error'
    for i in a:
        if i % 2 != 0:
            numeros_impares.append(i)
    if len(numeros_impares) < 1:
        return 'No hay numeros impares'
    return numeros_impares
            