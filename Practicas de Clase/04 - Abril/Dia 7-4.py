#%%
'''
Definir una funcion la cual te determine cual es carta que falta en una baraja de 40 cartas
1---10 Oro
11---20 Copa
21---30 Basto
31---40 Espada
'''
#Busqueda Lineal
def juego_de_cartas(carta_faltante):
    cartas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    for value in cartas:
        for subvalue in carta_faltante:
            if value not in carta_faltante:
                return value
print(juego_de_cartas([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40]))
#%%
'''
Definir una funcion la cual te determine cual es carta que falta en una baraja de 40 cartas
1---10 Oro
11---20 Copa
21---30 Basto
31---40 Espada
'''
#Busqueda Binaria
import time
def carta_faltante(maso1):
    primero=0
    ultimo=len(maso1)-1
    
    #la posicion 38 corresponde al ultimo elemento de la lista 
    
    while primero<=ultimo:
       mitad=(ultimo+primero)//2
       print("la mitad es",mitad)
       if maso1[mitad-1] == maso1[mitad]-2:
       #si falta la carta 20, el elemento 21 del elemento 19, estan consecutivos.
           return mitad+1
           
       elif maso1[mitad]==mitad+1:
           #cuando la carta es mayor a 20
           primero=mitad+1
           if maso1[mitad-1] == maso1[mitad]-2:
           #si la hay un salto de posicion en la lista, en elementos consecutivos, la carta se encuentra en ese valor    
               return mitad+1
       else:
           #cuando la carta es menor a 20
           ultimo=mitad-1
           
           if maso1[mitad-1] == maso1[mitad]-2:
           #si la hay un salto de posicion en la lista, en elementos consecutivos, la carta se encuentra en ese valor    
               return mitad+1
       time.sleep(1)
       if mitad==1:
           return 1
       
       
def main():
    maso1=[]
    cartaquefalta=5
    for i in range (1,41):
        maso1.append(i)
    print(maso1)
    del(maso1[cartaquefalta-1])
    print(maso1)
    print("la carta que falta es",carta_faltante(maso1))
main()
