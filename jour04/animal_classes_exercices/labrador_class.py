from dog_class import Dog

class Labrador(Dog):
    def __init__(self, name, hair_color, race="Labrador"): 
        super().__init__(name, race)
        self.__hair_color = hair_color

    def get_hair_color(self) : 
        return self.__hair_color
    def show_hair_color(self):
        print(f"The Labrador is {self.get_hair_color()} color")