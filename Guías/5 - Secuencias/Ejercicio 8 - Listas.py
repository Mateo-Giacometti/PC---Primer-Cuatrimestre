'''
Programar una función que tome como argumento un párrafo (un string con muchas palabras), y
retorne una lista indicando la frecuencia con la que ocurren palabras de distinta longitud (la estructura de
la lista a retornar queda a criterio del diseñador, pero debe ser explicada claramente en el docstring). Es
decir, la función debe computar cuantas palabras de largo 1 hay en el párrafo, cuantas de largo 2, y así
sucesivamente hasta la longitud más larga que tenga el párrafo.
'''
def text(parrafo: str) -> str:
    r = []
    p = []
    j = 1
    m = 0
    new_parrafo = parrafo.replace(',','').replace('.','').replace('?', '')
    for i in new_parrafo.split():
        r.append(len(i))
    while j < 20:    
        for i in r:
            if i == j:
                m += 1
        p.append(m)
        m = 0
        j+=1
    return p
    
            
        