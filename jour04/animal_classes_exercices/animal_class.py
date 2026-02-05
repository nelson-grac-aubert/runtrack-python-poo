class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def move(self): 
        print(f"{self.get_name()} is moving")