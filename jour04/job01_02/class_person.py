class Person : 
    def __init__(self) : 
        self.__age = 14

    def get_age(self) : 
        return self.__age
    def set_age(self, new_age : int) : 
        if type(new_age) == int and new_age >= 0 : 
            self.__age = new_age
        else : 
            print("Age must be a positive integer")
    
    def display_age(self):
        print(f"I am {self.get_age()} years old")
    
    def speak(self): 
        print("Hello")

        