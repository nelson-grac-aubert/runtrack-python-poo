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