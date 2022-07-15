#%%
#Ernesto
def intercalar(list1, list2):
    final_list = []
    i,v = 0,0
    while i < len(list1) and v < len(list2):
        if list1[i] < list2[v]:
            final_list.append(list1[i])
            i+=1
            if i == len(list1) and v < len(list2) :
                i-=1
        if list1[i] > list2[v]:
            final_list.append(list2[v])
            v+=1
            if v == len(list2) and i < len(list1):
                v-=1
        else:
            final_list.append(list1[i])
            final_list.append(list2[v])
            v+=1
            i+=1
    return final_list
print(intercalar([1,2,3,4,5,8],[2,4,6,8,10]))
#%%
#Alvaro
#Funcion que calcula potencias - Recursion
def power(x, h):
    if h == 0:
        return 1
    else:
        return power(x, h-1) * x
