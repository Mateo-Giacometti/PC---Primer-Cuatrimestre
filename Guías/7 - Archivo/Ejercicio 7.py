'''
Escribir una función, llamada grep, que reciba una cadena y un archivo, e imprima las líneas
del archivo que contienen esa cadena.
'''
def greep(filename, string):
    coincidence = ''
    with open(filename,'r') as read_file:
        for line in read_file:
            for words in (line.split()):
                if words == string:
                    coincidence += str(line).replace('\n', '') 
    return coincidence

                    
                    
                