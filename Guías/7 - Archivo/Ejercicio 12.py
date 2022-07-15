'''
Escribir una función, llamada sed, que reciba el nombre de un archivo, y dos cadenas. La
primera cadena en el archivo es la que queremos reemplazar por la segunda.
'''
def sed(filename,cadena,cadena2):
    with open(filename,'r') as write_file:
        replacement = ''
        for line in write_file:
            line = line.strip()
            changes = line.replace(cadena, cadena2)
            replacement = replacement + changes + "\n"
    write_file.close()
    with open("Text", "w") as write_file:
        write_file.write(replacement)
    write_file.close()
        
               
                            
                            
                
                
                
                
                           
            
        
    