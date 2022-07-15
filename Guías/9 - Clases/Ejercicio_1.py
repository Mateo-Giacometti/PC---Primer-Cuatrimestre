import math
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Cordenadas - Eje X: {self.x} - Eje Y: {self.y}'

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_norm(self):
        norm = math.sqrt(((self.x**2) + (self.y**2)))
        return norm

    def get_angle(self):
        angle = math.atan((self.y)/(self.x))
        return angle

    def distancia(self, other):
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2
        return (x_diff + y_diff)**0.5