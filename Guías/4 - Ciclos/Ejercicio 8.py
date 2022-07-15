'''
Escriba una función que devuelva el factorial de un número (entero).
'''
def factorial(n):
    result = 1
    if n == 0:
        return 1
    for i in range(1,n+1):
        result *= i
    return result 