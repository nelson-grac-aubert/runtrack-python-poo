from animal_class import Animal

class Dog(Animal): 
    def __init__(self, name, race):
        super().__init__(name)
        self.__race = race

    def move(self): 
        print(f"{self.get_name()} is running")

    def bark(self):
        print("Woof woof woof")

