def biyeccion(lista,elemento):
    inicio = 0
    final = len(lista) - 1
    medio = len(lista)//2
    while not (inicio > final):
        if lista[medio] == elemento:
            return print(f'Elemento se encuentra en la posicion {medio}')
        elif lista[medio] < elemento:
            inicio = medio + 1
            medio = (inicio + final)//2
        else:
            final = medio - 1
            medio = (inicio + final)//2
    return print('Elemento no se encuentra en la lista')
            