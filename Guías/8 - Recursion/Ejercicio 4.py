'''
Escribir una función recursiva que calcule el n-ésimo número triangular (el número triangular de
n es 1 + 2 + 3 + ··· + n).
'''
def triangular(n):
    if n == 0:
        return 0
    else:
        return n + triangular(n-1)
    