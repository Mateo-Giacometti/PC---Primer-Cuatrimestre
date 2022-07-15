class GeometryFigure(object):
    def __init__(self, lados = []): 
        self.lados = lados 

class Triangle(GeometryFigure):
    def __init__(self, lados=[]):
        super().__init__(lados)
    
    def __repr__(self):
        return f'Triangulo - Vertices {self.lados}'

    def __eq__(self, other):
        if isinstance(other, Triangle):
            if (other.get_area() == self.get_area()) and (other.get_perimeter() == self.get_perimeter()):
                return True
            else:
                return False
        else:
            return 'No se pueden comparar estos objetos'
    
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

class Rectangle(GeometryFigure):
    def __init__(self, lados=[]):
        super().__init__(lados) 
    
    def __repr__(self):
        return f'Rectangulo - Vertices: {self.lados}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            if (other.get_area() == self.get_area()) and (other.get_perimeter() == self.get_perimeter()):
                return True
            else:
                return False
    
    def __lt__(self, other): 
        if (self.get_perimeter() < other.get_perimeter()):
            return True
        else:
            return False
    
    def draw(self):
        rectangule_representation = ""
        x_diff1 = (self.lados[0] - self.lados[2])**2
        y_diff1 = (self.lados[1] - self.lados[3])**2
        altura = (x_diff1 + y_diff1)**0.5
        x_diff2 = (self.lados[2] - self.lados[4])**2
        y_diff2 = (self.lados[3] - self.lados[5])**2
        base = (x_diff2 + y_diff2)**0.5
        for i in range(altura):
            for v in range(base):
                rectangule_representation += '*'
            rectangule_representation += '\n'
        return print(rectangule_representation)

    def get_area(self):
        area = (1/2) * abs(((self.lados[0]*self.lados[3])+(self.lados[2]*self.lados[5])+(self.lados[4]*self.lados[7])+(self.lados[6]*self.lados[1]))-
        ((self.lados[1]*self.lados[2])+(self.lados[3]*self.lados[4])+(self.lados[5]*self.lados[6])+(self.lados[7]*self.lados[0])))
        return area
    
    def get_perimeter(self):
        x_diff1 = (self.lados[0] - self.lados[2])**2
        y_diff1 = (self.lados[1] - self.lados[3])**2
        dist1 = (x_diff1 + y_diff1)**0.5
        x_diff2 = (self.lados[2] - self.lados[4])**2
        y_diff2 = (self.lados[3] - self.lados[5])**2
        dist2 = (x_diff2 + y_diff2)**0.5
        x_diff3 = (self.lados[4] - self.lados[6])**2
        y_diff3 = (self.lados[5] - self.lados[7])**2
        dist3 = (x_diff3 + y_diff3)**0.5
        x_diff4 = (self.lados[6] - self.lados[0])**2
        y_diff4 = (self.lados[7] - self.lados[2])**2
        dist4 = (x_diff4 + y_diff4)**0.5
        return dist4 + dist3 + dist2 + dist1



a = Triangle([0,0,0,10,5,4])

print(a.get_area())