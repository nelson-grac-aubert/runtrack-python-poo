class Part:
    def __init__(self, name, material): 
        self.__name = name
        self.__material = material

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def get_material(self):
        return self.__material
    def set_material(self, new_material):
        self.__material = new_material

    def __str__(self): 
        return f"A {self.get_name()} made of {self.get_material()}"