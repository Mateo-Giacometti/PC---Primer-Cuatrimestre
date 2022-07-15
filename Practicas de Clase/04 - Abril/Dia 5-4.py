#%%
#Ernesto
'''
Contruir una funcion wildcard (patron:str, palabra:str) ->bool
El patron puede incluir 1 o mas ? 
'''
def wildcard (palabra_user, palabra_clave):
    x = -1
    for i in range (len(palabra_user)):
            if (palabra_user[i] != palabra_clave[i] and palabra_clave[i] != '?'):
                print(i)
                return False
            if ((palabra_user[i] == palabra_clave[i]) or (palabra_clave[i] == '?')):
                x = x + 1
    if x == i:
        return True
print(wildcard('hola', 'hola'))
#%%
#Alvaro
'''
Defina a function that removes from a given array of integars all the value contained in
a second array
'''

def remove_all_marked(array_one,array_two):
    result = []
    for value in array_one:
        for subvalue in array_two:
            if value not in array_two:
                result.append(value)
    return result
print(remove_all_marked([1,2,3,4,8,8,4,2,4], [4,8]))

#%%
#Alvaro 
'''
Write a function with the following properties:
    
- takes two lists
- returns a list of all possibilities to pair as many elements as possible from both lists while keeping the order 
of the elements
- output format is a list of lists of tuples, or a list with an empty list, if no pairs are possible
- inner lists can be of any order (see tests)

Hints

If both input lists are of equal length, then every item of one list will be paired with an item of the other list 
(see first example) -> results in only one sublist. If both input lists are of different length and not empty,
then every item of the shorter list will be paired, but not every item of the larger list -> results in more 
than one
sublist, because there are more then one possibilities to omit items from the larger list.

Example 1

Pair elements of ['c', 'o', 'd', 'e'] with elements of ['w', 'a', 'r', 's']

Expected Result:
    
[[('c', 'w'), ('o', 'a'), ('d', 'r'), ('e', 's')]]
'''
def list_of_tuples(list_one, list_two):
    lista =[]
    for first, second in zip(list_one, list_two):
        lista.append((first, second))
    return lista
print(list_of_tuples(['c','o','d','e'], ['w','a','r','s']))

#%%
#Alvaro
'''
Hacer lo mismo que en el ejercicio anterior, pero cada tupla debe mostrar un elemento junto al resto de los
elementos de las 2 listas
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    