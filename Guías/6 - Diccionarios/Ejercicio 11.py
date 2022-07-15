'''
Escribir un archivo llamado words.py que contenga una variable que sea una lista con palabras
(strings). Escribir, luego, una función que lea las palabras en words.py y las almacene como valores en
un diccionario. La clave a la que pertenece cada palabra es su propia longitud. Luego se pueden
recuperar rápidamente todas las palabras de una determinada longitud.
'''
from words import palabras

def pala():
    dic = {}
    for i in palabras:
        dic[len(i)] = i
    print(dic)
pala()
        
