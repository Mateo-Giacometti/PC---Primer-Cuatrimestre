'''
Escribir una función que permita determinar si una cadena podría formar una palabra, del siguiente
modo: el carácter "?" sirve de comodín para cualquier letra, mientras que sea 1 (una) letra, por lo que "?oca"
puede formar la palabra "poca", también la palabra "boca", o "roca". La palabra "?" puede formar cualquier
cadena de largo 1, mientras que "?o?a" puede formar "poca", "bota", "rosa", etc.
'''
def matches(palabra,codigo):
    if len(palabra) != len(codigo):
        return False
    for indice in range(len(palabra)):
        if codigo[indice] == '?':
            continue
        elif palabra[indice] != codigo[indice]:
            return False
    return True
