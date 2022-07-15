'''
La suma de Gauss permite hallar el resultado de sumar los numeros naturales entre 1 y n, es
decir: 1 + 2 + ... + (n - 1) + n. Escriba una funcion que compute esta suma (iterando) y que tenga como
entrada el numero n.
'''
def gauss(n):
    a = 0
    for i in range (0,(n+1)):
        a += i
    return a
    