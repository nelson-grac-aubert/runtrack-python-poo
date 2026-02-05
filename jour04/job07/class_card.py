class Card:
    
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
    
    def set_score(self, values_dic): 
        """ Determine the points of a card depending on its printed value """

        for key in values_dic : 
            if self.get_value() == key : 
                self.__score = values_dic[key]
        
        if self.get_value() == "ace" : 

            while True :

                choice = input("You've drawn an ace : type 1 or 11 to determine its points :")
                
                if choice != "11" and choice != "1" : 
                    print("Input error : only type 1 or 11")
                elif choice == "11" : 
                    self.__score = 11
                    break
                else : 
                    self.__score = 1 
                    break
                

