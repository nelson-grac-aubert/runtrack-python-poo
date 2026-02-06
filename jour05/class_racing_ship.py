from class_ship import Ship

class RacingShip(Ship):

    def __init__(self, parts, max_speed): 
        super().__init__(parts)
        self.__max_speed = max_speed

    def get_speed(self): 
        return self.__max_speed
    
    def display_speed(self): 
        print(f"\nMaximum speed of this ship : {self.get_speed()}")

    def display_state(self):
        super().display_state()
        print(f"Its max speed is of {self.get_speed()} knots")