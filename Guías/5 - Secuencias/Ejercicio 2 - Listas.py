'''
Programar una función que elimine todas las ocurrencias de un cierto elemento en una lista.
'''
def borrar(lista,b):
    for i in lista:
        if i == b:
            lista.remove(i)
    return lista
