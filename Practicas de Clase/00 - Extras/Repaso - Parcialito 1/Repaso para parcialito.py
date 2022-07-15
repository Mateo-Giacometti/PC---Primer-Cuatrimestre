#%%
#Recursividad
def pinos(n):
    if n == 1:
        return 1
    else:
       return pinos(n-1) + n
   
def filas(pins):
    i = 1
    while pinos(i) < pins:
        i += 1
    return i

#%%
def songs(filename):
    dic = {}
    with open(filename,'r') as f:
        for line in f:
            lista = line.split(' ')
            for i in lista:
                new_list = i.split(':')
                if new_list[0] in dic:
                    dic[(new_list[0])] = dic[new_list[0]] + int(new_list[1])
                else:
                    dic[(new_list[0])] = int(new_list[1])
    return print(dic)

#%%
def top_10(dic):
    lista = []
    other_list = []
    final_list = []
    for i in dic:
        lista.append(dic[i])
    lista.sort(reverse=True)
    lista = lista[0:10]
    for h in lista:
        if h in other_list:
            continue
        else:
            other_list.append(h)
    for v in other_list:
        for i in dic:
            if dic[i] == v:
                final_list.append(i)
    if len(final_list) > 10:
        final_list = final_list[0:10]
    return final_list
                
            


