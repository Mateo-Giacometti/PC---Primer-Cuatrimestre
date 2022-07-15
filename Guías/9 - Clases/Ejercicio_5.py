from Ejercicio_2 import Triangle
from Ejercicio_3 import Rectangle

a = Triangle([0,0,2,0,1,3])
b = Rectangle(3,4)
c = Triangle([0,0,2,0,1,3])
d = Rectangle(3,4)
e = Triangle([0,0,2,0,1,5])
f = Rectangle(7,2)

print(a == c)
print(a == e)
print(b == d)
print(b == f)