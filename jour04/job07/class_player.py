class Player : 
    def __init__(self) : 
        self.__cards = []
        self.__score = 0 
    
    def get_cards(self):
        return self.__cards
    def draw_card(self, new_card): 
        self.__cards.append(new_card)

    def get_score(self):
        return self.__score
    def update_score(self, points): 
        self.__score += points

    def draw_ace_behavior(self): 
        while True :

            choice = input("\nYou've drawn an ace : type 1 or 11 to determine its points :\n")

            if choice != "11" and choice != "1" : 
                print("Input error : only type 1 or 11")
            elif choice == "11" : 
                self.__score += 11
                break
            else : 
                self.__score += 1 
                break