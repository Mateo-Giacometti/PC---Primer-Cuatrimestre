'''
Escribir una función load_data que reciba un nombre de archivo, cuyo contenido tiene el
formato key:value, y devuelva un diccionario con el primer campo como clave y el segundo como
diccionario.
'''
def load_data(filename):
    dic = {}
    with open(filename,'r') as write_file:
        for line in write_file:
            line = (line.replace('\n', '')).split(':')
            dic[line[0]] = line[1]
    return dic