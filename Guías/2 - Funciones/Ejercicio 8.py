#%%
'''
La ecuación para el interés simple es:
donde:

Cn es el capital al inicio del período,

k es la cantidad de períodos,

Cn+k es el capital pasados los k períodos,

i es la tasa de interés nominal por período.

Escriba:
-Una función que dada una tasa de interés anual, una cantidad de años y un capital inicial, retorne el
capital al finalizar el período.
'''
def capita_final(i,k,Cn):
    capital = Cn * (1 + k*i)
    return capital
    
#%%    
'''
-Un programa que pida al usuario los datos necesarios y muestre en la consola interactiva el resultado
de ejecutar la función desarrollada.
'''
#%%
def capita_final():
    i = int(input('Ingrese el valor de la tasa de interes anual: '))
    k = int(input('Ingrese el valor de la cantidad de años: '))
    Cn = int(input('Ingrese el valor del capital inicial: '))
    capital = Cn * (1 + k*i)
    print('El capital al finalizar el periodo es de:',capital)
capita_final()
#%%