'''
Programar una función que tome una lista y elimine todos los elementos duplicados.
'''
def borrar(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2
