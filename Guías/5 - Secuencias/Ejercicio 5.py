'''
Una dirección IP (IPv4) es una cuarteto de números entre 0 y 255 (inclusive) separados por ".", y es la
dirección única de cada dispositivo conectado a una red, como la dirección postal de una casa en una
ciudad. Escribir una función que dada una dirección IPv4 válida, devuelva una versión modificada de esa
dirección IP, a esta versión modificada la llamaremos "IP con colmillos". Una dirección IP con colmillos
reemplaza cada punto "." de la dirección IP original con "[.]".

En la tabla siguiente se muestran pares entrada/salida para la función:

IPv4 IP con colmillos

"1.1.1.1" "1[.]1[.]1[.]1"

"255.100.50.0" "255[.]100[.]50[.]0"
'''
#%%
def IP(ip):
    result = ""
    for i in ip:
        if i == ".":
            result += "[.]"
        else:
            result += i
    return result
#%%
#Otra forma de hacerlo 
def good_ip(ip):
    ip = ip.replace('.','[.]')
    return ip 
#%%
#Otra forma de hacerlo
def another_good_ip(ip):
    ip = ip.split('.')
    return '[.]'.join(ip)