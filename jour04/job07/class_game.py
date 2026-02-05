import time
from class_card import Card
from class_deck import Deck
from class_player import Player
from class_dealer import Dealer
from class_human import Human

class Game() : 

    def __init__(self):
        self.turn = 0
        self.deck = Deck() 
        self.player = Human()
        self.dealer = Dealer()
        self.dealer_stopped_playing = False
        self.player_stopped_playing = False
        print("\nA game has been started and will start soon, have fun :)")
        time.sleep(2)

    def first_deals(self): 
        # Deal two cards each 
        self.deck.deal(self.player)
        self.deck.deal(self.dealer)
        self.deck.deal(self.player)
        self.deck.deal(self.dealer)


    def play_turns(self) : 

        while self.game_end_conditions() == False :

            self.turn += 1 

            if self.turn %2 == 1 : 
                decision = self.player.next_turn_behavior()
                if decision == "play" : 
                    self.deck.deal(self.player)
                else : 
                    self.player_stopped_playing = True
                    continue
            else : 
                decision = self.dealer.next_turn_behavior()
                if decision == "play" : 
                    self.deck.deal(self.dealer)
                else : 
                    self.dealer_stopped_playing = True
                    continue


    def game_end_conditions(self) : 
        if self.dealer_stopped_playing == True and self.player_stopped_playing == True : 
            return True
        if self.player.get_score() >= 21 : 
            return True
        if self.player.get_score() >= 21 : 
            return True 
        return False

    def loop(self): 
        self.first_deals()
        self.print_game_state()

        self.play_turns()

    
    def print_game_state(self): 
        print(f"\n--------------- The player's hand is : {self.player.get_cards()}")
        print(f"The player has {self.player.get_score()} points and is {21 - self.player.get_score()} points away from 21\n")
        print(f"--------------- The dealers's hand is : {self.dealer.get_cards()}")
        print(f"The dealer has {self.dealer.get_score()} points and is {21 - self.dealer.get_score()} points away from 21\n")
        print(f"--------------- The deck still contains : {self.deck.get_cards()}")