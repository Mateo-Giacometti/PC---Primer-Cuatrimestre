'''
Escribir una función que cuente la cantidad de letras A que se encuentran en una palabra. Complete
el siguiente código:

def count_A(the_string: str) -> int:
#complete me
'''
def count_A(the_string) -> int:
    contador = 0
    for i in the_string:
        if i.lower() == 'a':
            contador += 1
    return contador

        
        
    
