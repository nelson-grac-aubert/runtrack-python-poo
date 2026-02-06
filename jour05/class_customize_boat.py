from class_ship import Ship
from class_part import Part
import time

class CustomizeShip() : 
    def __init__(self) : 
        self.game_loop()

    def create_part(self) : 
        """ Return a new part made with the characteristics given by user inputs """
        print("\nLet's add a part to your boat :)")

        time.sleep(2)
        while True : 
            name = input("\nWhat kind of part is it? type its name and press enter")
            if name == "" : 
                print("\nEmpty entry, the part must have at least a character")
            else : 
                break
        
        time.sleep(2)
        while True : 
            material = input(f"\nWhat is that {name} made of? type its material and press enter")
            if material == "" : 
                print("\nEmpty entry, the material must have at least a character")
            else : 
                break
        
        time.sleep(1)
        print(f"\n Ok, so we're making a {name} made of {material}")
        return Part(name, material)

    def start_your_boat(self): 
        print("\nLet's start your ship with just one part for now :)")

        self.__ship = Ship({"1":self.create_part()})

    def check_boat_state(self): 
        self.__ship.display_state()

    def game_loop(self): 
        
        self.start_your_boat()
        time.sleep(2)
        self.check_boat_state()
