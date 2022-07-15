'''Cartuchera es un recepytaculo que contiene cosa (utiles). Tiene una capacidad y los utiles tienen un tamaño.
Los utiles pueden ser lapices, lapiceras y reglas. Hay que modelara esa relacion entre cartuchera y utiles y pensar
el comportamiento de meter cosas en la cartuchera, preguntar si hay elementos y sacar elementos de la cartuchera.
'''
class cosa(object):
    def __init__(self,size):
        self.size
class cartuchera(cosa):
    def __init__(self,size,capacidad):
        super().__init__(size)
        self.capacidad = capacidad
        self.cosas_dentro=[]
    
    def meter(self,util):
        if util.size > self.size:
            print('El tamaño del util es mayor al de la cartuchera')
        else:
            if len(self.cosas_dentro) >= self.capacidad:
                print('la cartucher esta llena')
    
class util(cosa):
    def __init__(self,length):
        super().__init__(length)
        
class lapiz(util):
    def __init__(self,length):
        super().__init__(length)
        
class lapicera(util):
    def __init__(self,length):
        super().__init__(length)
        
class regla(util):
    def __init__(self,length):
        super().__init__(length)
    
    
    
        
    
        
        