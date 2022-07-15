'''
Implemente una función que solicite un número por la consola, que represente el radio de una
circunferencia, y muestre en pantalla el perímetro de dicha circunferencia. En la consola se debe ver lo
siguiente:

Ingrese un valor que representa el radio de una circunferencia: [ENTRADA]
El perímetro resultante es [RESULTADO]
'''
def perimetro_de_circunferencia():
    radio = int(input('Ingrese un valor que representa el radio de una circunferencia: '))
    pi = 3.141592653589793
    perimetro = 2 * pi * radio
    return print('El perímetro resultante es',perimetro)
perimetro_de_circunferencia()