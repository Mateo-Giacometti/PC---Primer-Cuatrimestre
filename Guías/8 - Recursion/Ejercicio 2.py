'''
Implementar una función recursiva que retorne la cantidad de dígitos de un número entero.
'''
#%%
def dig_num(number: int) -> int:
    if len(str(number)) == 1:
        return 1
    else:
        return dig_num(int(str(number)[:-1])) + 1
    
    
print(dig_num(12556))
#%%
#Otra forma 
def digitos(numbers):
    if len(str(numbers)) == 1:
        return 1
    else:
        return digitos(numbers//10) + 1
print(digitos(12556))