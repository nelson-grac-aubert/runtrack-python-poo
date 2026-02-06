from class_ship import Ship
from class_part import Part
import time

class CustomizeShip() : 
    def __init__(self) : 
        self.__ship = Ship({})
        self.game_loop()

    def get_ship(self) : 
        return self.__ship

    def get_user_string(self, what) : 
        while True : 
            input_string = input(f"\nWhat is that {what}? type its name and press enter ")
            if input_string == "" : 
                print(f"\nEmpty entry, the {what} must have at least a character")
            else : 
                break
        return input_string
    
    def create_part(self) : 
        """ Return a new part made with the characteristics given by user inputs """
        print("\nLet's create that part!")

        time.sleep(2)
        name = self.get_user_string("part")
        
        time.sleep(2)
        print(f"\nLet's decide the {name}'s material")
        time.sleep(2)
        material = self.get_user_string("material")
        
        time.sleep(1)
        print(f"\nOk, so we're making a {name} made of {material}, it's been added to your boat!")
        return Part(name, material)

    def replace_part(self): 
        print("\nLet's replace an existing part with a new one :)")
        time.sleep(2)

        print(f"\nEnter the valid name of the part you want to replace")
        time.sleep(1)
        name = self.get_user_string("name")
        time.sleep(2)

        print(f"\nLet's replace that {name} with a brand new part")
        time.sleep(1)
        new_part = self.create_part()
        time.sleep(2)

        self.get_ship().replace_part(name, new_part)

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
        print("3 : change a part's material")
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

        while True : 
            choice = self.get_user_choice()
            if choice == "1" : 
                self.add_part_to_ship()
            if choice == "2" : 
                self.replace_part()
            elif choice == "4" : 
                self.check_ship_state()

            time.sleep(2)
                

