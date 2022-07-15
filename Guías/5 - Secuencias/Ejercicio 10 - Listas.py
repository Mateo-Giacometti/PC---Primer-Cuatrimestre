'''
En este ejercicio practicaremos el concepto de filtrado: queremos quedarnos con algunos elementos
de entre otros tantos, para ello:

Escribir una función que reciba una lista y retorne True o False dada alguna condición sobre sus
elementos. Por ejemplo, una función que recibe una lista de al menos 3 elementos y retorna True si
el segundo es mayor al tercero y la suma de estos dos es mayor 20.

Escribir una función llamada filtrar que recibe una lista L y una función f y retorne una lista con
aquellos elementos de L que al aplicarles f (al ejecutar f con cada uno de ellos como argumento,
individualmente) devuelven True.

Resolver el ejercicio anterior utilizando la función filtrar desarrollada en el inciso anterior.
'''
#%%
def f(lista):
    if len(lista) == 3:
        for i in lista:
            if type(i) == str or type(i) == bool:
                return False
        if lista[1] < lista[2]:
            return True
        else:
            return False 
    else:
        return False
    
def filtrar(lista):
    result = []
    for i in lista:
        if f(i):
            result.append(i)
    return result
            
        
    