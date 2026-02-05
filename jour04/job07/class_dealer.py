from class_player import Player

class Dealer(Player) : 
    def __init__(self):
        super().__init__()

    def next_turn_behavior(self): 
        if self.get_score() <= 17 : 
            return "play"
        else : 
            print("\nThe dealer has passed and won't draw anymore")
            return "pass"

    def draw_ace_behavior(self):
        if self.get_score() <= 10 : 
            self.update_score(11)
        else : 
            self.update_score(1)