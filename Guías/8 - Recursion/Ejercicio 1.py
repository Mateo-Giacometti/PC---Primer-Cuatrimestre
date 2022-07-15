'''
Para cada inciso, implementá una función recursiva que reciba un número z y un entero k y
retorne:
1. z + k (sumando unos),
2. z * k (sumas sucesivas)
3. z ^ k (multiplicaciones sucesivas).
'''
#%%
#1
def sum_num(z,k):
    if k == 0:
        return z
    else:
        return sum_num(z+1, k-1)
#%%
#2
def sum_sucesiva(z,k):
    if k == 1:
        return z
    else:
        return sum_sucesiva(z, k-1) + z
#%%
#3
def mul_sucesiva(z,k):
    if k == 1:
        return z
    elif k == 0:
        return 1
    else:
        return mul_sucesiva(z, k-1) * z
    