from class_player import Player
from class_dealer import Dealer

class Card:

    def __init__(self, color, value): 
        self.__color = color
        self.__value = value

    def get_color(self):
        return self.__color
    def set_color(self, new_color):
        self.__color = new_color

    def get_value(self):
        return self.__value
    def set_value(self, new_value):
        self.__value = new_value

    def get_score(self): 
        return self.__score
    def set_score(self, player): 
        """ Determine the points of a card depending on its printed value """

        values_dic = {"two": 2,
                    "three": 3,
                    "four": 4, 
                    "five": 5,
                    "six": 6,
                    "seven": 7,
                    "eight": 8,
                    "nine": 9,
                    "ten": 10, 
                    "jack": 10,
                    "queen": 10,
                    "king": 10}

        for key in values_dic : 
            if self.get_value() == key : 
                self.__score = values_dic[key]
                player.update_score(self.get_score())
        
        if self.get_value() == "ace" : 
            self.__score = player.draw_ace_behavior()

    def __repr__(self): 
        """ A human representation of what the card is """

        return f"A {self.get_value()} of {self.get_color()}"                