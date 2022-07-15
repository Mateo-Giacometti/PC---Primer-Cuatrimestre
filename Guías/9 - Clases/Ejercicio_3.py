class Rectangle(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def __repr__(self):
        return f'Rectangulo - Base:{self.base} - Altura:{self.altura}'

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
        for i in range(self.altura):
            for v in range(self.base):
                rectangule_representation += '*'
            rectangule_representation += '\n'
        return print(rectangule_representation)

    def get_area(self):
        return (self.base) * (self.altura)
    
    def get_perimeter(self):
        return (self.base)*2 + (self.altura)*2



    


