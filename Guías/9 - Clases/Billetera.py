'''
Diseñar la clase Billetera, la billetera tiene capacidad
Diseñar la clase Billete, tiene denominacion 1, 5, 10, 50
Se puede meter billetes en la billetera
Se puede quitar billetes en la billetera
Crear un metodos para vaciar 2 billeteras y crear una nueva que cntenga los billetes de las 2 ateriores
Crear un metedos que permita reducir la cantidad de billetes en la billetera, sin alterar la cantidad de dinero que se posee
'''
#%%
from urllib3 import Retry

class Billetera(object):
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.cosas_dentro = []
    
    def __repr__(self):
        r = "Billetera de capacidad: " + str(self.capacidad) + "\n"
        r += "Contenido: " + str(len(self.cosas_dentro)) +  "\n"
        for billete in self.cosas_dentro:
            r += "- " + billete.__repr__() + "\n"
        return r

    def meter_billetes(self, other):
        if not isinstance(other, Billete):
            return f'Solo se pueden ingresar billetes a la billetera'
        else:
            if len(self.cosas_dentro) >= self.capacidad:
                return f'La billetera esta llena'
            else:
                self.cosas_dentro.append(other)

    def sacar_billetes(self,other):
        if not isinstance(other, Billete):
            return f'Solo se pueden sacar billetes a la billetera'
        else:
            if len(self.cosas_dentro) == 0:
                return f'La billetera esta vacia'
            elif other not in self.cosas_dentro:
                return f'Este billete no se encuentra en la billetera'
            else:
                self.cosas_dentro.remove(other)
    
    def vaciar_billetera(self):
        self.cosas_dentro = []
        return f'Se ha vaciado la billetera'

    def cantidad_de_dinero(self):
        money = 0
        for i in self.cosas_dentro:
            money += i.denominacion 
        return f'{money} pesos'
    
    def combinar(self, other):
        if not isinstance(other, Billetera):
            return f'Solo se pueden combinar billeteras'
        else:
            nueva_billetera = Billetera(self.capacidad + other.capacidad)
            nueva_billetera.cosas_dentro = self.cosas_dentro + other.cosas_dentro
            self.vaciar_billetera()
            other.vaciar_billetera()
        return nueva_billetera
    
    def reduction(self):
        D1 = Billete(1)
        D2 = Billete(5)
        D3 = Billete(10)
        D4 = Billete(50)
        valor = 0
        for i in self.cosas_dentro:
            valor += i.denominacion
        self.cosas_dentro = []
        while True:
            if valor >= 50:
                self.cosas_dentro.append(D4)
                valor -= 50
                continue
            if valor >= 10:
                self.cosas_dentro.append(D3)
                valor-=10
                continue
            if valor >= 5:
                self.cosas_dentro.append(D2)
                valor -= 5
                continue
            if valor >= 1:
                self.cosas_dentro.append(D1)
                valor -= 1
                continue
            break

class Billete(object):
    def __init__(self, denominacion):
        if denominacion not in (1,5,10,50):
            self.denominacion = None
        else:
            self.denominacion = denominacion

    def __repr__(self):
        return f'Billete de {self.denominacion} pesos'

mi_billetera = Billetera(5)
mi_billetera2 = Billetera(5)
b1 = Billete(1)
b2 = Billete(5)
b3 = Billete(10)
b4 = Billete(50)
b5 = Billete(1)
b6 = Billete(1)

# %%
