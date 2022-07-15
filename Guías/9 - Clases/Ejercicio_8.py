class Interval(object):
    def __init__(self, inicio, fin, paso=1):
        self.inicio = inicio
        self.fin = fin
        self.paso = paso
        self.next = inicio

    def step(self,paso):
        self.paso = paso
    
    def get_next(self):
        self.next += self.paso
        return self.next
    
    def has_next(self):
        if self.next + self.paso <= self.fin:
            return True
        else:
            return False 
    
interval = Interval(10,100)

interval.step(0.5)

while interval.has_next():
    print(interval.get_next())
    


