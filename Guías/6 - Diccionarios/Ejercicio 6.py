'''
Escribir un programa que guarde el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} en
una variable, pregunte al usuario por una divisa y muestre su símbolo por pantalla, o un mensaje de
aviso si la divisa no está en el diccionario.
'''
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
money = input('Ingrese el nombre de la moneda buscada: ')
if money.title() in monedas:
    print(monedas.get(money))
else:
    print('La moneda buscada no esta en la lista')