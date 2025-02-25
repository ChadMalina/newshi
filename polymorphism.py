import math
class Shape:
    def Area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(Shape):
    def __int__(self,radius):
        self.radius = radius
    def area2(self,radius):
        return  math.pi * (self.radius **2)

rectangle=Rectangle(5,6)
circle=Circle(6)

print(f"The Rectangle's area is {rectangle.area()}")
print(f"The Circle's area is {circle.area2(6)}")

