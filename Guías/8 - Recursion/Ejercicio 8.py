'''
 Implementar una función recursiva que calcule el máximo común divisor (gcd) de 2 enteros x e y.
El gcd de los enteros x e y es el mayor entero que divide a ambos números con resto cero.
Resuelva primero por fuerza bruta: comience a probar números desde y en orden descendiente.
Una mejora es utilizar la siguiente definición recursiva:
si y es igual a 0, entonces gcd(x, y) es x
si no gcd(x, y) es gcd(y, x % y).
Un tercer algoritmo es:
si m y n son iguales:
 m es el gcd
 si m es mayor a n:
el gcd(m, n) es gcd(m - n, n)
 si no:
 el gcd(m, n) es gcd(m, n - m)
'''
#%%
def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
#%%
#Otra forma
def mcd(m,n):
    if m == n:
        return m
    elif m > n:
        return mcd(m - n, n)
    else:
        return mcd(m, n - m)