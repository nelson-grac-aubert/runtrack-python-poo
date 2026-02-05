from animal_class import Animal
from dog_class import Dog
from bird_class import Bird
from labrador_class import Labrador

animal_1 = Animal("Ronron")
dog_1 = Dog("Rex", "Jack Russel")
bird_1 = Bird("Titi", "Yellow")

animal_1.move()
dog_1.move()
dog_1.bark()
bird_1.move()

labrador_1 = Labrador("Medor", "chocolate")
labrador_1.move()
labrador_1.bark()
labrador_1.show_hair_color()

# dog_1.show_hair_color() # error cause hair color is a method of labradors only