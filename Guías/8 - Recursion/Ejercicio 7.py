'''
Escribir una función recursiva que calcule el n-ésimo número de la sucesión de Fibonacci. La
misma se define como F_n = F_{n-1} + F_{n-2}, F_0 = F_1 = 1.
Dibuje un esquema (árbol de recursividad) de las llamadas recursivas para n = 6.
'''
def Fibonacci(n):
    if n < 2:
        return n 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)