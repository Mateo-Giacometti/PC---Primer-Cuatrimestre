'''
Escriba una función que imprima en pantalla los múltiplos de, a la vez, 7 y 23 (por ejemplo, 161
es múltiplo de ambos, 21 es múltiplo de 7 pero no de 23 y 46 es múltiplo de 23 pero no de 7).
Escribir un programa que pida al usuario dos números A y B e imprima en la pantalla todos los
números múltiplos de, a la vez, 7 y 23, en el intervalo [A, B).
Escribir un programa que pida al usuario cuatro números A, B, C, y D e imprima en la pantalla
todos los números múltiplos de, a la vez, C y D, en el intervalo [A, B).
'''
#%%
def multiplos_7_23(m):
    for i in range(0,m+1):
        if i % 7 == 0 and i % 23 == 0:
            print(i)
    return
#%%
def multiplos_a_b(a,b):
    for i in range(a, b):
        if i % 7 == 0 and i % 23 == 0:
            print(i)
    return
#%%
def multiplos_c_d(a,b,c,d):
    for i in range(a,b):
        if i % c == 0 and i % d == 0:
            print(i)
    return

    