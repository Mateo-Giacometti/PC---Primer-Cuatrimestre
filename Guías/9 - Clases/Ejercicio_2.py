
class Triangle(object):
    def __init__(self, lados = []):
        self.lados = lados 
       
    def __repr__(self):
        return f'Triangulo - Vertices {self.lados}'

    def __eq__(self, other):
        if isinstance(other, Triangle):
            if (other.get_area() == self.get_area()) and (other.get_perimeter() == self.get_perimeter()):
                return True
            else:
                return False
    
    def __lt__(self, other):
        if (self.get_perimeter() < other.get_perimeter()):
            return True
        else:
            return False
   
    def get_area(self):
        area = (1/2) * abs(self.lados[0]*((self.lados[3]) - self.lados[5]) + 
        self.lados[2]*(self.lados[5] - self.lados[1]) + self.lados[4]*(self.lados[1] - self.lados[3]))
        return area

    def get_perimeter(self):
        x_diff1 = (self.lados[0] - self.lados[2])**2
        y_diff1 = (self.lados[1] - self.lados[3])**2
        dist1 = (x_diff1 + y_diff1)**0.5
        x_diff2 = (self.lados[2] - self.lados[4])**2
        y_diff2 = (self.lados[3] - self.lados[5])**2
        dist2 = (x_diff2 + y_diff2)**0.5
        x_diff3 = (self.lados[4] - self.lados[0])**2
        y_diff3 = (self.lados[5] - self.lados[1])**2
        dist3 = (x_diff3 + y_diff3)**0.5
        return dist3 + dist2 + dist1
