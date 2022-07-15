'''
Programar una función my_max que tome por argumento una lista con números (int o float) y
retorne el número máximo.
'''
def my_max(lista):
    maximo = 0
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo