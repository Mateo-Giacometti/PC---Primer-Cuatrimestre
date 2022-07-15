'''
Escriba una función que imprima los números primos entre 0 y N, donde N es un parámetro de
la función.
'''
def primos(n):
    lista = []
    contador = 1
    test = False
    while contador < n:
        test = False
        contador += 1
        for i in range(2,contador):
            if contador % i == 0:
                test = True
        if not test:
            lista.append(contador)
    return lista

                
                
                
                
                
                
                
    