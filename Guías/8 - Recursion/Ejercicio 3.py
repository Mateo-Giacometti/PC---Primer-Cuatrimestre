'''
Implementar una función recursiva que reciba un entero no negativo e retorne dicho número
espejado, es decir, para el 1234 retorna 4321.
'''
def mirror(number: int) -> int:
    if len(str(number)) == 1:
        return number
    else:
        return int(str(number)[-1] + str(mirror(int(str(number)[:-1]))))
     
print(mirror(2458))
