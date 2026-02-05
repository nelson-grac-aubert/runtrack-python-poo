from class_shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius): 
        self.__radius = radius 
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, new_radius):
        self.__radius = new_radius

    def surface(self):
        return self.get_radius() ** 2 * math.pi
