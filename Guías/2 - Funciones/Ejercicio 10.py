#%%
'''
La ecuación para el cálculo de la tasa de interés efectiva donde:

i es la tasa de interés nominal,

n es la cantidad de períodos de composición (o frecuencia),

r es la tasa de interés efectiva.

Escriba:

-Una función que dada una tasa de interés nominal anual y períodos de composiciones mensuales
calcule la tasa efectiva anual para todo el año.
'''
def taza_efectiva(i,n):
    r = (1 + (i / (n * 12)) ** (n * 12)) - 1
    return r
#%%
'''
-Un programa que pida al usuario los datos necesarios y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada.
'''
def taza_efectiva():
    i = int(input('Ingrese el valor del interes nominal: '))
    n = int(input('Ingrese el valor de los períodos de composiciones mensuales: '))
    r = (1 + (i / (n * 12)) ** (n * 12)) - 1
    print('La tasa efectiva anual es de',r)
taza_efectiva()
    