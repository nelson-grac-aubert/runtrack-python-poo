import random
import time

from class_card import Card
from class_player import Player
from class_human import Human
from class_dealer import Dealer

class Deck: 

    def __init__(self): 
        self.start_game()

    def start_game(self): 

        colors = ["hearts", "clubs", "spades", "diamonds"]
        values = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

        all_cards = []
        for color in colors : 
            for value in values : 
                all_cards.append(Card(color, value))
        
        self.__cards = all_cards

    def get_cards(self):
        return self.__cards

    def deal(self, player) : 

        # Pick a card at random in the deck, remove it from the deck list
        choice = random.choice(self.get_cards())
        self.__cards.remove(choice)

        # Add it to the player list
        player.draw_card(choice)

        # Calculate its score automatically if "two"-"king", ask player input for "ace"
        choice.set_score(player)
    
        # Display 
        if type(player) == Human : 
            print(f"\nThe player has been dealt a {choice}")
            print(f"The player's score is now {player.get_score()} points")
        else : 
            print("\nThe dealer has been dealt a card")
        time.sleep(1)

        