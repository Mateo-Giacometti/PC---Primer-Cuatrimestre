#%%
#Multiplicacion - Perspectiva Recursiva
def mul_rec(a,b):
    if b == 1:
        return a
    else:
       return a + mul_rec(a,(b-1))
#%%
#Factorial - Perspectiva Interativa 
def fact_inter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result 
#%%
#Factorial - Perspectiva Recursiva
def fact_rec(n):
    if n == 1:
        return n
    else:
        return n*fact_rec(n-1)
#%%
#Fibonacci - Perspectiva Recursiva (Esta forma es ineficiente)
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#%%
#Fibonacci con memorización (Mas eficiente)
def fib_memorization(n,d):
    global num_fib_calls
    num_fib_calls += 1
    
    if n in d:
        return d[n] #Usa un diccionario para capturar los resultados intermedios de la recursion
    else:
        ans = fib_memorization(n-1, d) + fib_memorization(n-2, d)
        d[n] = ans
        return ans
    d = {0:1, 1:1}
    for i in (29,):
        global num_fib_calls
        num_fib_calls = 0
        print("fib of", i, "-->",fib_memorization(i, d))
        print("fib (x) called","-->",num_fib_calls)
#%%
#Ejercicio
def palindromo(s, inicio,fin):
    if inicio >= fin:
        return True
    if s[inicio] == s[fin]:
        return palindromo(s, inicio+1, fin-1)
    else:
        return False
#%%
#Otra resolucion
def palindromov2(s):
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        s[0] == s[-1] and palindromov2(s[1:-1])
#%%
#Ejercicio
def dardos(a):
    if a in (0,5,7):
        return True
    elif a in (1,2,3,4,5):
        return False
    else:
        return dardos(a-5) or dardos(a-7)
    
        
    
        
        
        
        
        
        
        
        
        
        
        