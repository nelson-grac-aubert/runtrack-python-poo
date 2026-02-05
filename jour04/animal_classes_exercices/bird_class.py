from animal_class import Animal

class Bird(Animal) : 
    def __init__(self, name, feather_color): 
        super().__init__(name)
        self.__feather_color = feather_color

    def move(self):
        print(f"{self.get_name()} flies away")

        
