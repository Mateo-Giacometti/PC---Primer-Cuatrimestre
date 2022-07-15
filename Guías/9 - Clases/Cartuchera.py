'''
Cartuchera contiene cosas
Generalente contiene útiles
Los útiles son lapices, lapiceras y reglas
La cartuchera tiene una capacidad y un tamaño
Los útiles tienen un tamaño
Se pide diseñar estos objetos y relaciones
Se pide meter y quitar un útil dentro de la cartuchera
Se pide saber si un útil está dentro de una cartuchera
Se pide listar los elementos de una cartuchera
'''
#%%
class Objetos(object):
    def __init__(self,size):
        self.size = size

class Cartuchera(Objetos):
    def __init__(self, size, capacidad):
        Objetos.__init__(self,size)
        self.size = size
        self.capacidad = capacidad
        self.cosas_dentro = []
    
    def __repr__(self):
        return f'Cartuchera - Size: {self.size} - Capacity: {self.capacidad}'
    
    def put_utiles(self, Utiles):
        if self.size < Utiles.size:
            return 'El objeto es muy grande como para entrar en la cartuchera'
        else:
            if len(self.cosas_dentro) >= self.capacidad:
                return 'La cartuchera ya esta llena'
            else:
                self.cosas_dentro.append(Utiles)
                return f'Se ha agregado {Utiles} a la cartuchera'
    
    def take_out_utiles(self, Utiles):
        if len(self.cosas_dentro) == 0:
            return 'La cartuchera esta vacia'
        else:
            if Utiles not in self.cosas_dentro:
                return 'Este util no esta en la cartuchera'
            else:
                self.cosas_dentro.remove(Utiles)
                return f'Se ha sacado {Utiles} de la cartuchera'

    def dentro_de_cartuchera(self):
        dentro = str(self.cosas_dentro).replace('[','').replace(']','')   
        return print(dentro)      

class Utiles(Objetos):
    def __init__(self, size):
        Objetos.__init__(self, size)
    
class Lapiz(Utiles):
    def __init__(self, size = 4):
        Utiles.__init__(self, size = size)
    
    def __repr__(self):
        return f'Lapiz'

class Lapicera(Utiles):
    def __init__(self, size = 5):
        Utiles.__init__(self, size = size)
    
    def __repr__(self):
        return f'Lapicera'

class Regla(Utiles):
    def __init__(self, size = 8):
        Utiles.__init__(self, size = size)
    
    def __repr__(self):
        return f'Regla'


a = Cartuchera(7,4)
b = Lapicera()
c = Lapiz()
d = Lapicera()
e = Lapicera()
f = Lapicera()

# %%
