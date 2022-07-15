'''
Escriba una función que dado un tiempo en segundos, retorne el tiempo en horas, minutos y
segundos (similar al ejercicio 12). Por ejemplo, para 3745 debe devolver 1, 2, 25
'''
seg = int(input('Ingrese lo segundos: '))
def segundos(seg):
    horas = seg // 3600
    seg = seg % 3600
    minutos = seg // 60
    segundos = seg % 60
    return print(f'Horas = {horas} - Minutos = {minutos} - Segundos = {segundos}')
segundos(seg)    