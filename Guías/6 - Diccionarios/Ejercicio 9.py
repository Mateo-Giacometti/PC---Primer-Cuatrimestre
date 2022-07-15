'''
Escribir una función que reciba la cantidad de iteraciones a realizar de una tirada de 2 dados y
devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
'''
import random
def frecuencia_de_tiradas(k):
    lista = []
    dic = {}
    cont = 1
    while k > 0:
        a = random.randint(1,6)
        b = random.randint(1,6)
        suma = a + b
        lista.append(suma)
        k-=1
    for i in lista:
        if i in dic:
            del dic[i]
            cont += 1
            dic[i] = cont
        else:
            dic[i] = 1
    return dic
        
    

        
