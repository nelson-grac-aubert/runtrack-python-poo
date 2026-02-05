import random

from class_card import Card
from class_player import Player

class Deck: 

    def __init__(self): 
        self.start_game()

    def start_game(self): 

        colors = ["heart", "club", "spade", "diamond"]
        values = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

        all_cards = []
        for color in colors : 
            for value in values : 
                all_cards.append(Card(color, value))
        
        self.__cards = all_cards

    def get_cards(self):
        return self.__cards

    def deal(self, player: Player) : 

        # Pick a card at random in the deck, remove it from the deck list
        choice = random.choice(self.get_cards())
        self.__cards.remove(choice)

        # Add it to the player list
        player.draw_card(choice)

        # Calculate its score automatically if "two"-"king", ask player input for "ace"
        choice.set_score(player)
        # Add the score to the player score