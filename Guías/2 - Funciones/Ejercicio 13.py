'''
Escriba una función que dado un número devuelva el primer número múltiplo de 10 inferior o
igual a él. Por ejemplo, para 153 debe devolver 150.
'''
def numero(n):
    if n % 10 == 0:
        return n
    else:
        while True:
            n -= 1
            if n % 10 == 0:
                return n 
                break
            else:
                continue
            
            