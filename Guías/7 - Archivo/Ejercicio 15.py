'''
Dado el siguiente archivo de texto, que contiene un guion de la serie Seinfeld:
1. Eliminar los nombres de los personajes.
2. Eliminar lineas en blanco.
3. Eliminar puntuaciones.
4. Eliminar informacion adicional para los actores.
5. Guardar el archivo con los cambios.
'''
def boca(filename):
    with open(filename,'r+') as file:
        actor = True
        parentesis = True
        replace = ''
        d = ''
        for i in file:
            for v in i:
                if v == ':':
                    actor = False
                    continue
                if actor == True:
                    continue
                if v == '(':
                    parentesis = False
                if parentesis == True and v not in '.,?':
                    d += v
                elif v == ')':
                    parentesis = True
            actor = True
            replace = replace + d 
            d = ''
    with open(filename,'w') as file2:
        file2.write(replace)

            
    