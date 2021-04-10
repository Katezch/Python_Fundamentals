'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"This is a rectangle with width {self.width} and length {self.length}."

    def area(self):
        return self.width*self.length

    def perimeter(self):
        return (self.width+self.length)*2


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"This is a circle with radius {self.radius}."

    def area(self):
        return self.radius * self.radius * 3.14

    def circumference(self):
        return 2*3.14*self.radius


rect1 = Rectangle(10, 16)
cir1 = Circle(2008)
print(rect1)
print(rect1.area())
print(rect1.perimeter())

print(cir1)
print(cir1.area())
print(cir1.circumference())

