'''
Diseñar la clase Billetera. La billetera tiene capacidad.
Diseñar la clase Billete. La clase tiene denominacion 1,5,10,50
Se pueden meter billetes en una billetera 
Se pueden quitar billetes en la billetera 
'''
from tkinter import N

class Billetera(object):
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.cosas_dentro = []
    
    def meter(self,billete):
        if not isinstance(billete, Billete):
            print('La billetera solo acepta billetes')
        elif len(self.cosas_dentro) >= self.capacidad:
            print('La billetera esta llena')
        else:
            self.cosas_dentro.append(billete)
    
    def quitar(self,billete):
        if billete in self.cosas_dentro:
            self.cosas_dentro.remove(billete)
        else:
            print('Este billete no esta en la billeteras')
    
    def __repr__(self):
        r = "Billete de capacidad: " + str(self.capacidad) + "\n"
        r+= "Contenido: " + str(len(str(self.cosas_dentro))) + "\n"

    def reduction(self):
    valor = 0
    for i in self.cosas_dentro:
        valor += i
    self.cosas_dentro = []
    while True:
        if valor >= 50:
            self.cosas_dentro.append(50)
            valor -= 50
            continue
        if valor >= 10:
            self.cosas_dentro.append(10)
            valor-=10
            continue
        if valor >= 5:
            self.cosas_dentro.append(5)
            valor -= 5
            continue
        if valor >= 1:
            self.cosas_dentro.append(1)
            valor -= 1
            continue
        break

class Billete(object):
    def __init__(self, denomonacion):
        if denomonacion not in (1,5,10,50):
            self.denominacion = None
        else:
            self.denominacion = denomonacion

    def __repr__(self):
        return 'Billete de: ' + str(self.denominacion)
        
        
        
    def division():
    la_billetera =[50,10,5,1,10,50]
    bille1 = []
    bille2 = []
    dic = {}
    for i in la_billetera:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] % 2 == 0:
            bille1.append((dic[i]/2))
            bille2.append((dic[i]/2))
        else:
            bille1.append

    

    







