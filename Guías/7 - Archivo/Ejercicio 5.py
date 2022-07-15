'''
Escribir una función, llamada cp, que copie todo el contenido de un archivo a otro, de modo
que quede exactamente igual.
'''
def cp(filename):
    with open(filename, 'r') as read_file:
        with open('Copia','w') as write_file:
            for line in read_file:
                write_file.write(line)
                