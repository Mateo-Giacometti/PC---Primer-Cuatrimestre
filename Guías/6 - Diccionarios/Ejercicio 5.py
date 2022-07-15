'''
Escriba una función que recibe una cadena y devuelve un diccionario con la cantidad de apariciones de cada carácter en la cadena.
'''
def apariciones(cadena):
    dic = {}
    for i in cadena:
        if i not in dic:
            dic[i] = cadena.count(i)
        else:
            continue
    return dic