class Operation():
    def __init__(self) : 
        self.nombre1 = 5
        self.nombre2 = 8

    def addition(self) : 
        self.result = self.nombre1 + self.nombre2
        print(f"{self.nombre1} + {self.nombre2} = {self.result}")

        return self.result
    
my_operation = Operation()
my_operation.addition()