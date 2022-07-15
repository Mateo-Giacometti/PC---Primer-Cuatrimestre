'''
Escriba una función que imprima K números equiespaciados entre dos números arbitrarios N y
M. Como lo hace esta función.
'''
def equispaciados(start, end,step):
    espacio = (end - start)/(step-1)
    result = [start]
    for i in range(step-2):
        result.append(start+espacio*(i+1))
    result.append(end)
    return result