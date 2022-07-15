'''
Escribir una función, llamada wc, que dado un archivo de texto, lo procese e imprima por
pantalla cuántas líneas, cuántas palabras, cuántos caracteres contiene el archivo, y el nombre del
archivo.
'''
def wc(filename):
    number_of_lines = 0
    number_of_words = 0
    number_of_caracters = 0
    with open(filename,'r') as read_file:
        for line in read_file:
            number_of_lines += 1
            for words in (line.split()):
                number_of_words += 1
                for caracters in range(len(words)):
                    number_of_caracters += 1
    information = print(number_of_lines,number_of_words,number_of_caracters,filename)
    return information
                    
                