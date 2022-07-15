'''
Escribir una función recursiva que dado un arreglo de números, retorne el máximo, usando
dividir y conquistar.
'''
def arreglo(v):
    if len(v) == 1:
        return v[0]
    if v[0] > v[1] or v[0]==v[1]:
        v.remove(v[1])
        return arreglo(v)
    elif v[0] < v[1]:
        v.remove(v[0])
        return arreglo(v)
    