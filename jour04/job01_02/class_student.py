from class_person import Person

class Student(Person) : 
    def __init__(self) : 
        super().__init__()
    
    def go_to_class(self): 
        print("I'm going to class")
    
        