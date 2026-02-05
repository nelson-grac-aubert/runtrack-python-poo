from class_card import Card
from class_deck import Deck
from class_player import Player
from class_dealer import Dealer

class Game() : 

    def __init__(self):
        self.__turn = 0
        self.deck = Deck() 
        self.player = Player()
        self.dealer = Dealer()

    def initialize(self): 
        # Initiate a game, a player, a dealer

        # Deal two cards each 
        self.deck.deal(self.player)
        self.deck.deal(self.dealer)
        self.deck.deal(self.player)
        self.deck.deal(self.dealer)
    
    def print_game_state(self): 
        print(f"--------------- The player's hand is : {self.player.get_cards()}")
        print(f"The player has {self.player.get_score()} points and is {21 - self.player.get_score()} points away from 21\n")
        print(f"--------------- The dealers's hand is : {self.dealer.get_cards()}")
        print(f"The dealer has {self.dealer.get_score()} points and is {21 - self.dealer.get_score()} points away from 21\n")
        print(f"--------------- The deck still contains : {self.deck.get_cards()}")