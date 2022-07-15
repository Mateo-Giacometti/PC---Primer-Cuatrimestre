'''
Escribir una función, llamada cat, que reciba dos cadenas referidas a los nombres de dos
archivos, y guarde en un tercer archivo el contenido de los dos archivos
'''
def cat(filename,otherfilename):
    with open(filename, 'r') as read_file:
        with open(otherfilename, 'r') as read_file2:
            with open('Copia','x') as write_file:
                for line in read_file:
                    write_file.write(line)
                for line2 in read_file2:
                    write_file.write(line2)
            
                    
        
        