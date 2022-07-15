'''
Escribir una función que reciba una fecha en formato AAAA-MM-DD y retorne un tupla de 3 enteros
con la fecha. En el formato AAAA-MM-DD, AAAA representa el año con 4 dígitos, MM el mes con 2 dígitos, y
DD el día con 2 dígitos.
'''
def fecha_a_numero(fecha):
    fecha_new = []
    new_fecha = fecha.split('-')
    for i in new_fecha:
        i = int(i)
        fecha_new.append(i)
    if fecha_new[0] > 9999:
        return False
    elif fecha_new[1] > 12:
        return False
    tupla_fecha = tuple(fecha_new)
    return tupla_fecha