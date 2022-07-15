'''
Implementar una función recursiva que dados dos números n y b retorne True si n es potencia
de b.
'''
def potencia(n,b):
    if b == n or n == 1:
        return True
    elif (n < b) or (b == 1 and n != 1) or (b == 0 and n != 0):
        return False
    else:
        return potencia(n/b, b)
        