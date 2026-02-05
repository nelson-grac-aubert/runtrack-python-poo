from class_vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.__door_count = 4 
    
    def get_door_count(self):
        return self.__door_count
    def set_door_count(self, new_door_count):
        self.__door_count = new_door_count
    
    def get_vehicle_info(self):
        super().get_vehicle_info()
        print(f"The vehicle's door count is {self.get_door_count()}\n")

    def start(self): 
        super().start()
        print("Let's ride on 4 wheels!")