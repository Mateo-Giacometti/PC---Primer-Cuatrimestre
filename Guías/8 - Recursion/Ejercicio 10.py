'''
El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera:
Las filas se enumeran desde n = 0, de arriba hacia abajo.
Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha).
Los valores que se encuentran en los bordes del triángulo son 1.
Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba.
'''
def Pascal(n,k):
    if n >= 0:
        if k == 0 or k == n:
            return 1
        else:
            return Pascal(n-1,k) + Pascal(n-1, k-1)
        
        
        
        