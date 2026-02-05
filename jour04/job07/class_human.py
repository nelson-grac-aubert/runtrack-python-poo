from class_player import Player

class Human(Player): 
    def __init__(self):
        super().__init__()
    
    def next_turn_behavior(self): 
        while True : 
            choice = input("\nYour turn : type y to draw, n to pass\n")

            if choice != "y" and choice != "n" : 
                print("Input error : only type y or n")
            elif choice == "y" : 
                return "play"
            else : 
                return "pass"

    def draw_ace_behavior(self): 
        while True :

            choice = input("\nYou've drawn an ace : type 1 or 11 to determine its points :\n")

            if choice != "11" and choice != "1" : 
                print("Input error : only type 1 or 11")
            elif choice == "11" : 
                self.update_score(11)
                break
            else : 
                self.update_score(1) 
                break