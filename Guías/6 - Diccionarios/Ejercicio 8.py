'''
Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las
claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
'''
def tuplas_a_diccionario(lista):
    dic = {}
    for i in lista:
        for v in range(len(i)):
            listina = []
            if i[v].title() in dic:
                (dic[i[v]]).append(i[v+1])
            if v == 0 and i[v].title() not in dic:
                listina.append(i[v+1])
                dic[i[v]] = listina
    return dic