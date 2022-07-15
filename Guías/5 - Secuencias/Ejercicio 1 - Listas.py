'''
Programar una función que tome una lista de números y compute la suma de todos los números en
la lista.
'''
def lista_de_numeros(lista):
    suma = 0
    for i in lista:
        suma += i
    return print('La suma de los numeros de la lista es igual a:',suma)
