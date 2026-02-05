class Vehicle:
    def __init__(self, brand, model, year, price) : 
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price 

    def get_brand(self):
        return self.__brand
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def get_model(self):
        return self.__model
    def set_model(self, new_model):
        self.__model = new_model

    def get_year(self):
        return self.__year
    def set_year(self, new_year):
        self.__year = new_year

    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

    def get_vehicle_info(self):
        print(f"\nThe vehicle's brand is {self.get_brand()}")
        print(f"The vehicle's model is {self.get_model()}")
        print(f"The vehicle's year is {self.get_year()}")
        print(f"The vehicle's price is {self.get_price()}")

    def start(self):
        print(f"Putting the key inside the slot...")