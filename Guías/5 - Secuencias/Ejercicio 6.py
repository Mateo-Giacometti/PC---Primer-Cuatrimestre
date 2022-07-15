'''
Algunos tipos de piedras son joyas, y todas las joyas son piedras. Vamos a representar cada piedra
con un carácter, por ejemplo la "a", por lo que una cadena de caracteres representa un conjunto de piedras,
por ejemplo "aaAb" es un conjunto de piedras. Dada una cadena de caracteres que representa los tipos de
piedras que son joyas, y otra cadena de caracteres que representa las piedras que tienes, quieres saber
cuántas joyas tienes, es decir, cuántas de las piedras que tienes son también joyas.

Las letras distinguen entre mayúsculas y minúsculas, por lo que "a" se considera un tipo de piedra diferente
de "A".
'''
def joyas_y_piedras(joyas,piedras):
    joyas_totales = 0
    for i in piedras:
        for v in joyas:
            if i == v:
                joyas_totales += 1
    return joyas_totales
                
        
    