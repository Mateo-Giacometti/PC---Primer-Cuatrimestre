'''
Escriba una función que imprima N números de la secuencia de Fibonacci, donde N es un
parámetro de la función.
'''
def Fibonacci(N):
    secuencia = [1]
    a = 0
    b = 1
    for i in range (N-1):
        c = a + b
        a = b
        b = c
        secuencia.append(b)
    return secuencia
        