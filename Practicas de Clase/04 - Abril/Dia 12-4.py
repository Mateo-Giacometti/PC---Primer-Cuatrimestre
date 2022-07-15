#%%
#Ernesto
'''
En un juego de dardos, el centro vale 7 puntos, el borde 5 y fuera vale 0. 
Dado un puntaje final, verificar si responde a un juego valido
'''
def juego_de_dardos(dardos):
    for i in range (0,100):
        for v in range (0,100):
            if (i*5 + v*7) == dardos:
                return True
            else:
                pass
    return False 
#%%   
#Ernesto             
'''
Dado un str, crear un programa que cree una diccionario que muestre la frecuencia de las letras de la palabra
'''
def contar_letras(palabra:str):
    d = {}
    for letra in palabra:
        if letra in d:
            d[letra] = d[letra] + 1
        else:
            d[letra] = 1
    return d
