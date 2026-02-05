from class_shape import Shape

class Rectangle(Shape): 
    def __init__(self, length, width) :
        self.__length = length 
        self.__width = width
    
    def get_length(self):
        return self.__length
    def set_length(self, new_length):
        self.__length = new_length

    def get_width(self):
        return self.__width
    def set_width(self, new_width):
        self.__width = new_width

    def surface(self) : 
        return self.get_length() * self.get_width()
