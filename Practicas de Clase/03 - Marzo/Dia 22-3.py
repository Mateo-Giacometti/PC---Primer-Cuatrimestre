#%%
for i in range (0,10):
    print(i)
#%%
for x in range (10,0,-1):
    print(x)
#%%
a = "hola"
for z in (a):
    print(z)
#%%
for i in range(2,9):
    print("Pregunto si",i,'es divisor de 9')
    es_divisor = (9 % i == 0)
    if es_divisor:
        print(i, "es divisor de 9")
    else:
        print(i, 'no es divisor de 9')
#%%
