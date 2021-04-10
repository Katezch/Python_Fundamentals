'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"This is a {self.year} {self.model} car that has a maximum speed of {self.max_speed}"

    def increase_speed(self):
        self.max_speed += 5

car1 = Car("BMW", 2021, 50)
car2 = Car("TSL", 2020, 60)

print(car1)
print(car2)

car1.increase_speed()
car2.increase_speed()
print(car1)
print(car2)