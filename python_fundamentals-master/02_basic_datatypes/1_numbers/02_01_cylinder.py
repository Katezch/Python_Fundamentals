'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math
def cylinder_volume(radius, height):
    return math.pi*radius*radius*height

def cylinder_surface_area(radius, height):
    return math.pi*radius*radius*2+2*math.pi*radius*height

print("sylinder volume is: ", cylinder_volume(3.14, 5))

print("surface area is: ", cylinder_surface_area(3.14, 5))

