'''
Escribir una función que reciba una lista de tuplas, donde cada tupla contiene un nombre y una fecha
(la fecha puede ser una tupla o una cadena en formato AAAA-MM-DD, a elección de quien programa la
función). La función debe retornar True si todas las personas son de sagitario. Considere el caso particular
en que la lista contenga 8 tuplas, los primeros 6 nombres sean "Gachi", "Pachi", "Lorena", "novio", "exnovio"
y "Andrea", y sean todos de sagitario, en cuyo caso debe imprimirse un mensaje acorde, además de retornar
el correspondiente True
'''
def cadena(fecha):
    for i in fecha:
        if(fecha.split('-')[1] == '11' and 22 <= int(fecha.split('-')[2]) <= 31) or (fecha.split('-')[1]=='12' and 1 <= int(fecha.split('-')[2]) <= 21):
            return True
        return False

def returner(lista: list)->bool:
    count=0
    for tupla in lista:
        fecha = tupla[1]
        if cadena(fecha)==True:
            count+=1
    if count==len(lista):
        return True
    return False

print (returner([("Gachi", "2004-11-29"),("pachi", "2004-12-12")]))
            
        
        
        
    