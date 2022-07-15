'''
Sistema Sexagesimal

El sistema sexagesimal representa angulos/tiempo en horas/grados, minutos y segundos

A = 10 grados 30 minutos y 50 segundos
B = 10 grados 30 minutos 20 segundos

Si los sumo (A+B)

Segundos: 50 + 20 es mas que 60 y me paso 1 minutos (me quedo con 10 segundos).

Minutos: 30 + 30 + 1 = 61. Me llevo 1 y me quedo con 1 munuto.

Grados: 10 + 10 + 1 = 21

A+B = 21 grados 60 minutos 60 segundos

Se pide modelar un sistema sexagesimal y modelar la suma, resta, igualdad y mayor. 

'''
from re import X

class Sexagesimal(object):
    def __init__(self, grados, minutos, segundos):
        self.grados = grados
        self.minutos = minutos
        self.segundos = segundos
        self.correccion()
    
    def __repr__(self):
        return f"{self.grados}º {self.minutos}' {self.segundos}\""

    def correccion(self):
        while self.segundos > 60:
            self.minutos += 1
            self.segundos -= 60
        while self.segundos < 0:
            self.minutos -= 1
            self.segundos += 60
        while self.minutos > 60:
            self.grados += 1
            self.minutos-= 60
        while self.minutos < 0:
            self.grados -= 1
            self.minutos += 60
        while self.grados > 360:
            self.grados -= 360
        while self.grados < 0:
            self.grados += 360 
    
    def __add__(self, other):
        sum = Sexagesimal((self.grados + other.grados),(self.minutos + other.minutos),(self.segundos + other.segundos))
        sum.correccion()
        return sum
    
    def __sub__(self, other):
        res = Sexagesimal((self.grados - other.grados),(self.minutos - other.minutos),(self.segundos - other.segundos))
        res.correccion()
        return res 
    
    def __eq__(self, other):
        if (self.segundos == other.segundos) and (self.minutos == other.minutos) and (self.grados == other.grados):
            return True 
        else:
            return False 
    
    def __lt__(self, other):
        if self.grados > other.grados:
            return True
        elif self.grados == other.grados:
            if self.minutos > other.minutos:
                return True 
            elif self.minutos == other.minutos:
                if self.segundos > other.segundos:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
