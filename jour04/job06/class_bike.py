from class_vehicle import Vehicle

class Bike(Vehicle): 
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.__wheel_count = 2
    
    def get_wheel_count(self):
        return self.__wheel_count
    def set_wheel_count(self, new_wheel_count):
        self.__wheel_count = new_wheel_count
    
    def get_vehicle_info(self):
        super().get_vehicle_info()
        print(f"The bike's wheel count is {self.get_wheel_count()}\n")
    
    def start(self): 
        super().start()
        print("Let's ride on 2 wheels!")