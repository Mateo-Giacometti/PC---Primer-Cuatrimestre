'''
Escriba una función que devuelva el número combinatorio para un par de números n, k.
'''
def factorial_a(n):
    result = 1
    if n == 0:
        return 1

    for i in range(1,n+1):
        result *= i
    return result 

def numero_combinatorio(n,k):
    return factorial_a(n)/factorial_a(k)*factorial_a(n-k)