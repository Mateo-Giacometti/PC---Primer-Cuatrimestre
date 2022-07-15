'''
Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las
claves sea el primer elemento de la tupla y el valor el segundo, asumir que nunca estarán repetidas las
claves
'''
def lista_de_tuplas_a_diccionario(lista):
    dic = {}
    for i in lista:
        for v in range(len(i)):
            if v == 0:
                dic[i[v]] = i[v+1]
    return dic
            