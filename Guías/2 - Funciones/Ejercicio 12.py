'''
Escriba una función que dadas la hora, minutos y segundos devuelva el tiempo en segundos.
Escriba un programa que pida la hora al usuario y muestre el tiempo en segundos.
'''
h = int(input('Ingrese las horas: '))
m = int(input('Ingrese los minutos: '))
s = int(input('Ingrese los segundos: '))
def match_duration(hours, minutes, seconds):
    duracion = (hours * 3600) + (minutes * 60) + seconds
    return print('\nEsto equivale a', duracion, 'segundos')
match_duration(h,m,s)
