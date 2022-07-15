#%%
#Crear una funcion que verifique la validez de una ip
def ip_is_invalid(ip):
    lista = ip.split('.')
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    for v in lista:
        if lista[v] <= 0 or lista[v] >= 256:
            return True
    return False
#%%
#Otra opcion 
def ip_is_invalid_op(ip):
    lista = ip.split('.')
    for value in lista:
        if int(value) <= 0 or int(value) >= 256:
            return True
    return False

    