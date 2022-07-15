'''
Escriba un programa que calcule una aproximación a la función exponencial, sin utilizar la
función exponencial de python.
'''
def factorial_a(n):
    result = 1
    if n == 0:
        return 1

    for i in range(1,n+1):
        result *= i
    return result 

def exponential_aprox(x):
    N = 100
    result = 0
    for i in range(0,N):
        result += x**i/factorial_a(i)
    return result