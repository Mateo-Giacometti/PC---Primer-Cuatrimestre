#%%
'''
Escriba una función que redondee un número de tipo flotante al entero más cercano y devuelva
este número entero.
'''
def redondeo(numero):
    return round(numero)
#%%
'''
Escriba un programa que pida al usuario el número y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada.
'''
def redondeo():
    numero = float(input('Ingrese un numero no entero: '))
    return print(round(numero))
redondeo()
#%%