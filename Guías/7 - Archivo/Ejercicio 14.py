'''
Un archivo TSV (Tab Separated Value) es un archivo, similar al CSV. Donde cada espacio es un caracter tabular; en ASCII es el código 09 (distinto al caracter espacio).
Escribir una función que reciba la información que se quiere escribir en un archivo en formato TSV.
Esta información tiene que estar estructurada en una secuencia de secuencias.
'''
def TSV(info):
    with open('TSV','w') as file:
        for i in info:
            file.write(str(i).replace('[', '').replace(']','').replace('"','').replace("'", '').replace('(', '').replace(')','').replace(',', '    ') + '\n')

