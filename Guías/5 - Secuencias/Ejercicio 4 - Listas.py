'''
Programar una funcion que tome dos listas y retorne True si las listas tienen por lo menos un
elemento en comun.
'''
def listas(lista1,lista2):
    for i in lista1:
            if i in lista2:
                return True
    return False
    
    