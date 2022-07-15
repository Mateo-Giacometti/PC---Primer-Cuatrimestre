'''
Un archivo CSV (Comma Separated Value) es un archivo de texto que, en cada línea, almacena
un registro. Cada registro está compuesto por campos. En el archivo, cada campo está separado por
comas (,), de ahí el nombre. El siguiente texto es un ejemplo del contenido de un archivo con el
mencionado formato:
Escribir una función que reciba la información que se quiere escribir en un archivo en formato CSV.
Esta información tiene que estar estructurada en una secuencia de secuencias.
'''
def CSV(info):
    with open('CSV','w') as file:
        for i in info:
            file.write(str(i).replace('[', '').replace(']','').replace('"','').replace("'", '').replace('(', '').replace(')','') + '\n')
            
    