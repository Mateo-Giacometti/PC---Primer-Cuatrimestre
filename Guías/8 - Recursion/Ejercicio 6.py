'''
Escribir una función recursiva que encuentre el mayor elemento de un vector.
'''
def vector(v):
    if len(v) == 1:
        return v[0]
    if v[0] > v[1] or v[0]==v[1]:
        v.remove(v[1])
        return vector(v)
    elif v[0] < v[1]:
        v.remove(v[0])
        return vector(v)
        
    