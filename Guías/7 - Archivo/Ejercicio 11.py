'''
 Escribir una función save_data que reciba un diccionario y un nombre de archivo, y guarde el
contenido del diccionario en el archivo, con el formato key:value.
'''
def save_data(diccionario):
    with open('Keys', 'w') as file:
        for i in diccionario:
            clave = str(i)
            conten = str(diccionario[i])
            file.write((clave+':'+conten+'\n'))
    