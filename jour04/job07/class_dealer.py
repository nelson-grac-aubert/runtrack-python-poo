from class_player import Player

class Dealer(Player) : 
    def __init__(self):
        super().__init__()

    def draw_ace_behavior(self):
        if self.get_score() <= 10 : 
            self.update_score(11)
        else : 
            self.update_score(1)