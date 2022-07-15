'''
Escriba una función que recibe un número y devuelve un diccionario cuyas claves son desde el
número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
'''
num = int(input('Ingrese numero: '))
def cuadrados(num):
    dic = {}
    for i in range (1, num + 1):
        dic[i] = i**2
    return dic
print(cuadrados(num))