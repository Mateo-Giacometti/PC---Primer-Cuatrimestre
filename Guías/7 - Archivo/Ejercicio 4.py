'''
Escribir una función, llamada touch, que reciba el nombre del archivo a guardar, y genere una
archivo de texto vacío.
'''
def touch(filename):
    file = open(filename,'x')
    file.close()