from class_ship import Ship
from class_part import Part
import time

class CustomizeShip() : 
    def __init__(self) : 
        self.__ship = Ship({})
        self.game_loop()

    def get_ship(self) : 
        return self.__ship

    def create_part(self) : 
        """ Return a new part made with the characteristics given by user inputs """
        print("\nLet's add a part to your ship :)")

        time.sleep(2)
        while True : 
            name = input("\nWhat kind of part is it? type its name and press enter ")
            if name == "" : 
                print("\nEmpty entry, the part must have at least a character")
            else : 
                break
        
        time.sleep(2)
        while True : 
            material = input(f"\nWhat is that {name} made of? type its material and press enter ")
            if material == "" : 
                print("\nEmpty entry, the material must have at least a character")
            else : 
                break
        
        time.sleep(1)
        print(f"\nOk, so we're making a {name} made of {material}, it's been added to your boat!")
        return Part(name, material)

    def add_part_to_ship(self) : 
        new_part = self.create_part()
        self.get_ship().add_part(new_part)
        
    def start_your_ship(self): 
        print("\nLet's start your ship with just one part for now :)")

        self.add_part_to_ship()

    def get_user_choice(self): 
        print("\n ----- Here are your next options -----")
        print("1 : add a part to your ship")
        print("2 : replace a part with another")
        print("3 : change a piece completely")
        print("4 : display the current state of your ship")

        while True : 
            choice = input("Type 1, 2 or 3 and press enter ") 
            if choice not in ["1", "2", "3","4"] : 
                print("Input error : just type the number")
            else : 
                return choice

    def check_ship_state(self): 
        self.__ship.display_state()


    def game_loop(self): 
        
        self.start_your_ship()
        time.sleep(2)
        self.check_ship_state()
        time.sleep(2)

        while True : 
            choice = self.get_user_choice()
            if choice == "1" : 
                self.add_part_to_ship()
            elif choice == "4" : 
                self.check_ship_state()

            time.sleep(2)
                

