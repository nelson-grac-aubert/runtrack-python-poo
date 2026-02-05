from class_rectangle import Rectangle

class Parallelepiped(Rectangle): 
    def __init__(self, length, width, height) : 
        super().__init__(length, width)
        self.__height = height
    
    def get_height(self):
        return self.__height
    def set_height(self, new_height):
        self.__height = new_height
    
    def volume(self) : 
        return self.surface() * self.get_height()