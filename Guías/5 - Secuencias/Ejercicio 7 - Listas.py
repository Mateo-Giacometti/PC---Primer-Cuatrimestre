'''
Programar una función llamada terminan_en_vocal que tome por argumento una lista de strings,
y devuelva otra lista con los strings que terminan en vocal.

Pueden probar la función con las palabras que surgen de aplicar la función split al preámbulo de la
Constitución Nacional.
'''
def terminan_en_vocal(lista):
    lista2 = []
    for i in lista:
        if ('a' == i[(len(i) - 1)].lower() or 'e' == i[(len(i) - 1)].lower() or 'i' == i[(len(i) - 1)].lower() 
        or 'o' == i[(len(i) - 1)].lower() or 'u' == i[(len(i) - 1)].lower()):
            lista2.append(i)
    return lista2

                
            