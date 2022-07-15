'''
 Escribir una función que reciba una lista de listas y elimine todas las listas cuyo 3er elemento sea
mayor a un número dado. Por ejemplo, si se tiene la lista: [["W", 5, 31], ["U", 7, 18], ["F",
11, 15], ["B", 16, 28]], y el número 20, debe devolver la lista [["U", 7, 18], ["F", 11,
15]]
'''
def lista_de_listas(lista: list, num: int) -> list:
    sub_list = []
    contador = -1
    for i in lista:
        contador += 1
        sub_list.append(i)
        if i[2] > num:
            del sub_list[contador]
            contador -= 1
    return sub_list
#%%
#Otra opcion 
def lista_de_listas1(lista: list, num: int) -> list:
    sub_list = []
    for i in lista:
        if i[2] < num:
            sub_list.append(i)
    return sub_list